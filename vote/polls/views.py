from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from polls.models import Subject, Teacher, User
from polls.utils import gen_random_code, gen_md5_digest
from polls.captcha import Captcha
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.serializer import SubjectSerializer
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection
import json

# @api_view(('GET', ))
# @cache_page(timeout=86400, cache='default')
# def show_subjects(request):
#     """获取学科数据"""
#     queryset = Subject.objects.all()
#     data = SubjectSerializer(queryset, many=True).data
#     return Response({'code': 20000, 'subjects': data})
def show_subjects(request):
    """获取学科数据"""
    redis_cli = get_redis_connection()
    # 先尝试从缓存中获取学科数据
    data = redis_cli.get('vote:polls:subjects')
    if data:
        # 如果获取到学科数据就进行反序列化操作
        data = json.loads(data)
    else:
        # 如果缓存中没有获取到学科数据就查询数据库
        queryset = Subject.objects.all()
        data = SubjectSerializer(queryset, many=True).data
        # 将查到的学科数据序列化后放到缓存中
        redis_cli.set('vote:polls:subjects', json.dumps(data), ex=86400)
    return JsonResponse({'code': 20000, 'subjects': data})

@api_view(('GET', ))
def display_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by('no')
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)

# def show_subjects(request):
#     subjects = Subject.objects.all().order_by('no')
#     return render(request, 'subjects.html', {'subjects': subjects})

def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            print(sno)
            subject = Subject.objects.only('name').get(no=sno)
            print(subject)
            print(subject.name)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')

def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        if captcha:
            print(captcha)
            print(request.session['captcha'])
            if captcha.lower() == request.session['captcha'].lower():
                if username and password:
                    password = gen_md5_digest(password)
                    user = User.objects.filter(username=username, password=password).first()
                    if user:
                        request.session['userid'] = user.no
                        request.session['username'] = user.username
                        return redirect('/')
                    else:
                        hint = '用户或登录名错误'
                else:
                    hint = '请输入有效的用户名和密码'
            else:
                hint = '验证码错误'
        else:
            hint = '请输入验证码'
    return render(request, 'login.html', {'hint': hint})

def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')

def get_captcha(request: HttpRequest) -> HttpResponse:
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')
