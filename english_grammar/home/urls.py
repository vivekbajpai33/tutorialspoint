from django.urls import path
from .views import *

urlpatterns = [
    path('edit/coursese/<int:id>/', EditCourses, name='edit-courses'),
    path('delete/courses/<int:id>/', DeleteCourses, name='delete-courses'),
    path('class/', Videoclass, name='classes')
]
