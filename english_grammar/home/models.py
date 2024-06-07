from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=100 ,null=True, blank=True)
    subject_code = models.CharField(max_length=100 ,null=True, blank=True)

    def __str__(self):
        return self.subject_name


class courses(models.Model):
    subjectname =  models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    paid = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        ordering = ['subjectname']


class StudentQuery(models.Model):
    query = models.CharField(max_length=500, null=True, blank=True)
    solution = models.CharField(max_length=500, null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=100 , null=True, blank=True)  

class Notification(models.Model):
    notification = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)


class BlogStory(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    story = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)


class classes(models.Model):
    courses = models.ForeignKey(Subject, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="video_thumb" ,null=True, blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='class_video', null=True, blank=True ,validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'webm', 'avi', 'mkv'])])
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    # def __str__(self):
    #     return self.courses.subjectname   








