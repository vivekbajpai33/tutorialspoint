from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

# models
from home.models import *


# login required
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    course= courses.objects.all()
    story = BlogStory.objects.all()
    sutdent_query = StudentQuery.objects.all()
    content = {
        'courses':course,
        'story': story,
        'query':sutdent_query,
    }
    if request.method == 'POST':
       query = request.POST.get('student_query')
       sutdent_query = StudentQuery.objects.create(query=query)
       return redirect('/')
    return render(request, "home/dashboard.html", content)


def EditCourses(request, id):
    object =courses.objects.get(id=id)
    context = {
        'data':object
    }

    if request.method == 'POST':
        subject = request.POST.get('subject')
        code = request.POST.get('code')
        description = request.POST.get('description')
        object.subject_name = subject
        object.subject_code = code
        object.description = description
        object.save()
        return redirect('/courses/')
    return render(request, 'home/edit_courses.html' , context)


def DeleteCourses(request, id):
    object = courses.objects.get(id=id)
    object.delete()
    return redirect('/courses/')


def Videoclass(request):
    video = classes.objects.all()
    course = courses.objects.all()
    content = {
        'data':video,
        'object' : course
    }

    if request.method == 'POST':
        subject  = request.POST.get('courses')
        course = courses.objects.get(id=subject)
        video = request.POST.get('video')
        title = request.POST.get('title')
        data = classes.objects.create(courses=course, video=video, title=title)
        return render(request, 'home/classes.html', content)
    return render(request, 'home/classes.html', content)



def studentData(request):
    student = User.objects.all()
    return render(request, 'home/student-data.html', {'data':student})

def DeleteStudent(reuqest,id):
    student = User.objects.get(id=id)
    student.delete()
    return redirect('/our-courses/student-data/')
    


