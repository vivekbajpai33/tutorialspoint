from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# import userforeignkey
from django_userforeignkey.models.fields import UserForeignKey

class Trackable(models.Model):
    creted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = UserForeignKey(related_name='created_%(class)s' ,auto_user_add=True, on_delete=models.CASCADE, blank=True, null=True)
    updated_by = UserForeignKey(related_name='modified_%(class)s' ,auto_user=True, blank=True, null=True )

    def __str__(self):
        return self.created_by

    # class Meta:
    #     abstract =True


# Create your models here.

class Subject(models.Model):
    created_by = UserForeignKey(related_name='created_%(class)s' ,auto_user_add=True, on_delete=models.CASCADE, blank=True, null=True)
    subject_name = models.CharField(max_length=100 ,null=True, blank=True)
    subject_code = models.CharField(max_length=100 ,null=True, blank=True)

    def __str__(self):
        return self.subject_name


class courses(models.Model):
    subjectname =  models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notes = models.FileField(upload_to="notes/", null=True, blank=True, default=None)
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
    thumbnail = models.ImageField(upload_to="videothumb/", null=True, blank=True, default=None)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to="classvideo/", null=True, blank=True ,validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'webm', 'avi', 'mkv'])])
    title = models.CharField(max_length=200, null=True, blank=True)    
    
    # def __str__(self):
    #     return self.courses.subjectname   








