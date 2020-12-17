from django.shortcuts import render, redirect
from django.http import JsonResponse
from polls.models import Teacher, Teacher

def praise_or_criticize(request):
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 200, 'msg': '操作成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 500, 'msg': '操作失败'}
    else:
        data = {'code': 401, 'msg': '请先登录'}
    return JsonResponse(data)