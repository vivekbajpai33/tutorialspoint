from django.shortcuts import render,redirect, HttpResponse
from django.views import View

# django messages
from django.contrib import messages


# import user model 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# import login, logout 
from django.contrib.auth import login, logout


# login decoreter
from django.contrib.auth.decorators import login_required


# models 
from home.models import courses



# Create your views here.

def Login(request):    
    if request.method == 'POST':  
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = authenticate(username=username, password=password)
        if student is not None:
          login(request, student)
          return redirect('/')
        else:
           messages.error(request, "Something went wrong please try again.")
           return render(request ,'home/login.html')             
        return redirect('/')
    return render(request ,'home/login.html')


def signup(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      number = request.POST.get('number')
      password = request.POST.get('password')
      student = User.objects.create_user(username=username, email=email, first_name=number, password=password)
      login(request, student)
      return redirect('/')
   return render(request, "home/sign_up.html")


def Logout(request):
   logout(request)
   return redirect('/')


def about(request):
   return render(request, 'home/about.html')


def profile_edit(request, id):
   user = User.objects.get(pk=id)
   context = {
      'data' : user
   }
   if request.method == 'POST':
      username = request.POST.get('name')
      email = request.POST.get('email')
      number = request.POST.get('number')
      user = User.objects.get(pk=id)
      user.username = username
      user.email = email
      user.first_name = number
      user.save()
      return redirect('/')
   return render(request, 'home/profile_page.html', context)


def Courses(request):
   item = courses.objects.all()
   context = {
      'data' : item
   }
   if request.method == 'POST':
      subject_name = request.POST.get('subject_name')
      code = request.POST.get('subject_code')
      description = request.POST.get('description')
      paid = request.POST.get('paid')
      our_courses = courses.objects.create(subject_name=subject_name, subject_code=code, description=description, paid=paid)
      return redirect('/')
   
   return render(request, 'home/courses.html' , context)
