from django.shortcuts import render, redirect

# from polls.models import Subject, Teacher
# # Create your views here.
#
# def show_subjects(request):
#     subjects = Subject.objects.all().order_by('no')
#     return render(request, 'subject.html', {'subjects': subjects})
#
# def show_teacher(request):
#     try:
#         sno = int(request.GET.get('sno'))
#         teacher = []
#         if sno:
#             subject = Subject.objects.only('name').get(no=sno)
#             teachers = Teacher.objects.filter(subject=subject).order_by('no')
#         return render(request, 'teacher.html', {
#             'subject': subject,
#             'teachers': teachers
#         })
#     except (ValueError, Subject.DoesNotExist):
#         return redirect('/')