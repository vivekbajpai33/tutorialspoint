from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required

# models
from home.models import *


# login required
from django.contrib.auth.decorators import login_required
from authentication.views import login

# api 
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


# Create your views here.
def home(request):
    course= courses.objects.all().order_by('-id')[:4]
    story = BlogStory.objects.all().order_by('-id')[:4]
    sutdent_query = StudentQuery.objects.all().order_by('-id')[:4]
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
    subject = Subject.objects.all()
    cours =courses.objects.get(id=id)
    context = {
        'data':cours,
        'subject':subject
    }

    if request.method == 'POST':
        new_subject = request.POST.get('subject')
        subject = Subject.objects.get(id=new_subject)
        title = request.POST.get('title')
        description = request.POST.get('description')
        notes = request.FILES.get('notes')
        paid= request.POST.get('paid')
        if notes is not None:
            cours.notes = notes
            cours.subjectname = subject
            cours.description = description
            cours.save()
            return redirect('/courses/')
        cours.subjectname = subject
        cours.description = description
        cours.title = title
        cours.paid = paid
        cours.save()
        return redirect('/courses/')
    return render(request, 'home/edit_courses.html' , context)

def DeleteCourses(request, id):
    object = courses.objects.get(id=id)
    object.delete()
    return redirect('/courses/')

@login_required
def Videoclass(request):
    video = classes.objects.all()
    course = Subject.objects.all()
    searchvideo = request.GET.get('search-video')
    content = {
        'data':video,
        'object' : course
    }
    if searchvideo:
        print(searchvideo)
        video = classes.objects.all().filter(title__icontains=searchvideo)  
        content = {
            'data':video
        }
        return render(request, 'home/classes.html', content)      

    if request.method == 'POST':
        subject  = request.POST.get('courses')
        course = Subject.objects.get(id=subject)
        video = request.FILES['video']
        title = request.POST.get('title')
        description = request.POST.get('description')
        thumbnail = request.FILES['thumbnail']
        data = classes.objects.create(courses=course, video=video, title=title, description=description, thumbnail=thumbnail)
        return render(request, 'home/classes.html', content)
    return render(request, 'home/classes.html', content)

def Editclass(request, id):
    data = classes.objects.get(id=id)
    cours = courses.objects.all()
    context = {
        'object':data,
        'courses':cours
    }
    if request.method == 'POST':
        video_cours = request.POST.get('cours')
        thumb = request.FILES.get('thumbnail')
        video = request.FILES.get('video')
        title = request.POST.get('title')
        video_courses = Subject.objects.get(id=video_cours)
        data.courses = video_courses
        data.thumbnail = thumb
        data.video = video
        data.title = title
        data.save()
        return redirect('classes')
    return render(request, 'home/edit_video_class.html', context)


def studentData(request):
    student = User.objects.all()
    user = request.user.groups.all()
    print(user)
    context = {
        'data': student,
        'groups' : Group.objects.all(),
        'user_droup' : user   
    }
    if request.method == 'POST':
        user_group = request.user.groups.all()
        group = request.POST.get('')
        user_group = group
        
          
    return render(request, 'home/student-data.html', context)

def DeleteStudent(reuqest,id):
    student = User.objects.get(id=id)
    student.delete()
    return redirect('/our-courses/student-data/')
    
def deletevideo(request, id):
    cours = classes.objects.get(id=id)
    cours.delete()
    return redirect('classes')


# classed based api
class VideoApi(APIView):

    def get(self, request):
        video_class = classes.objects.all()
        serializers = VideoSerializers(video_class, many=True)
        return Response(serializers.data, status.HTTP_200_OK)
     
# function based api of Subject model
@csrf_exempt
def SubjectApiView(request):
    query_set = Subject.objects.all()
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    serilizer = SubjectSerializers(query_set, many=True)
    return JsonResponse(serilizer.data, safe=False)  

@api_view(['GET','POST'])
def StudentqueryView(request):
    query_set = StudentQuery.objects.all()
    try:
        if request.method == 'GET':
            serializer = StudentquerySerializers(query_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)

    except:
        if request.method == 'POST':
            serializer = StudentquerySerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def ContactView(request):
    query_set = Contact.objects.all()
    try:
        if request.method == 'GET':
            serializer = ContactSerializers(query_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)
    except:
        if request.method == 'POST':
            serializer = ContactSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           





