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
    path('student-data/delete/<int:id>/', DeleteStudent, name='delete-student'),
    path('video-api/', VideoApi.as_view(), name='video'),
    path('subject-api/', SubjectApiView, name='subject_api'),
    path('student-query-api/', StudentqueryView, name='student_query'),
    path('contact-api/', ContactView),
    path('delete-class/<int:id>/', deletevideo, name='delete-class'),
    path('edit/class-video/<int:id>/', Editclass, name='editvideo')
]
