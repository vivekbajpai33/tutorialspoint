from django.urls import path
from .views import *

# add api url
from rest_framework import routers

router = routers.DefaultRouter()
from rest_framework import routers

router = routers.DefaultRouter()



urlpatterns = [
    path('edit/coursese/<int:id>/', EditCourses, name='edit-courses'),
    path('delete/courses/<int:id>/', DeleteCourses, name='delete-courses'),
    path('class/', Videoclass, name='classes'),
    path('student-data/', studentData, name='user-data'),
    path('student-data/delete/<int:id>/', DeleteStudent, name='delete-student')
]
