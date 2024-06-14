from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Subject)
class AllSubject(admin.ModelAdmin):
    list_display =['id', 'created_by', 'subject_name']
    search_fields = ['subject_name']


@admin.register(courses)
class OurCourses(admin.ModelAdmin):
    list_display = ['subjectname', 'paid']
    list_filter = ['subjectname']
    search_fields = ['subjectname']

@admin.register(StudentQuery)
class Query(admin.ModelAdmin):
    list_display = ['query', 'solution']
    search_fields = ['query'] 


@admin.register(Notification)
class notification(admin.ModelAdmin):
    list_display = ['notification', 'date']
    list_filter = ['notification', 'date'] 
    search_fields = ['date']


@admin.register(BlogStory)
class story(admin.ModelAdmin):
    list_display = ['title', 'story']

@admin.register(Contact)
class contact(admin.ModelAdmin):
    list_display = ['name', 'number']  

@admin.register(classes)
class video(admin.ModelAdmin):
    list_display = ['courses', 'title']       
    list_filter = ['courses', 'upload_date']
    search_fields = ['courses']
    

