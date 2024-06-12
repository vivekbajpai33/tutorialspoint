from django.shortcuts import render,redirect, HttpResponse
from django.views import View
from .form import CaptchForm,ChangePasswordForm
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm
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
from home.models import courses,Subject

# send mail
from django.core.mail import send_mail
from django.conf import settings

# api view
from rest_framework import viewsets
from .serializers import UserSerializers,CoursesSerializers,AddCoursesSerializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view



# Create your views here.

def Login(request):    
    if request.method == 'POST':  
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = authenticate(request, username=username, password=password)
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
         captcha_form = CaptchForm(request.POST)   
      # custom user register
         username = request.POST.get('username')
         email = request.POST.get('email')
         number = request.POST.get('number')
         password = request.POST.get('password')
         if captcha_form.is_valid():
           student = User.objects.create_user(username=username, email=email, first_name=number, password=password)
           user =  authenticate(request, username=username, password=password)
           login(request, user)
           send_mail (
            'Welcome In Vmec',  # subject,
            f'Hello {username} welcome you ', #message,
            'bajpaivivek878@gmail.com',  #kon send kar raha hai,
            [email],#user (list me send karna hai like[email]),
            fail_silently = False
          )
           return redirect('/')
         else : 
          return redirect('/register/sign-up/')
   captcha_form = CaptchForm()      
   context = {
      'form' : captcha_form
   }      
   return render(request, "home/sign_up.html", context)


def ResetPassword(request):
   if request.method == 'POST':
      form = PasswordResetForm(request.POST)
      if form.is_valid():
         return redirect('/register/change-password/')
      else : 
         return redirect('/register/reset-password/')   
   form = PasswordResetForm()   
   context = {
      'form' : form
   }   
   return render(request, "home/reset_password.html", context)      


def ChangePassword(request):
   if request.user.is_authenticated:
      current_user = request.user
      if request.method == 'POST':
         form = ChangePasswordForm(current_user, request.POST)
         if form.is_valid():
            form.save()
            # login(request, current_user)
            return redirect('/register/login/')
         else:
            return redirect('/register/change-password/')
      else:
         form =ChangePasswordForm(current_user)
         return render(request, "home/change_password.html", {'form':form})
   else:
      return redirect('/')   
   

def Logout(request):
   logout(request)
   return redirect('/')


def about(request):
   return render(request, 'home/about.html')


@login_required
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

@login_required
def Courses(request):
   item = courses.objects.all().order_by('-id')
   subject_data = Subject.objects.all()
   context = {
      'data' : item,
      'subject' : subject_data
   }
   if request.method == 'POST':
      subject_name = request.POST.get('subject_name')
      subject = request.POST.get('subject')
      subject_code = request.POST.get('subject_code')
      paid = request.POST.get('paid')
      courses_subject = Subject.objects.get(id=subject_name)
      description = request.POST.get('description')
      title = request.POST.get('title')
      Notes = request.FILES.get('notes')
      if subject:
         sub = Subject.objects.create(subject_name=subject, subject_code=subject_code)
         sub.save()
         return redirect('courses')
      elif Notes is not None:       
         our_courses = courses.objects.create(subjectname=courses_subject, title=title , description=description, notes=Notes, paid=paid)
         return redirect('courses')
      else:
         our_courses = courses.objects.create(subjectname=courses_subject, title=title , description=description, notes=None, paid=paid)
         return redirect('courses')   
   return render(request, 'home/courses.html' , context)





# create api view 
class UserApiView(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializers


class CoursesApiView(APIView):
   # permission_classes = [AllowAny]
   item = courses.objects.all()

   def get(self, request):     
     serializer = CoursesSerializers(self.item, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)
   
class AddCoursesView(APIView):
   def post(self, request):
      serializer = AddCoursesSerializers(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)   

class EditCoursesApiView(APIView):

    def get_object(self, pk):
        return courses.objects.get(pk=pk)
      

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = CoursesSerializers(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = CoursesSerializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   #  def patch(self, request, pk):
   #      book = self.get_object(pk)
   #      serializer = BookSerializer(book, data=request.data, partial=True)
   #      if serializer.is_valid():
   #          serializer.save()
   #          return Response(serializer.data)
   #      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   #  def delete(self, request, pk):
   #      item = self.get_object(pk)
   #      item.delete()
   #      return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteCoursesApi(APIView):

   def get_obj(self, pk):
      return courses.objects.get(pk=pk)
   
   def delete(self, request, pk):
      item = self.get_obj(pk)
      item.delete()
      return Response(status=status.HTTP_200_OK)



