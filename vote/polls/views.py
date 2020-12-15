from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from polls.models import Subject, Teacher, User
from polls.utils import gen_random_code, gen_md5_digest
from polls.captcha import Captcha
# Create your views here.

def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})

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
