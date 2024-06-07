from rest_framework import serializers
from .models import classes,Subject,StudentQuery,Contact


class VideoSerializers(serializers.ModelSerializer):
    courses_obj = serializers.SerializerMethodField()

    def get_courses_obj(self, obj):
        return {'cours': obj.courses.subject_name}

    class Meta:
        model = classes
        fields = ['courses_obj', 'upload_date', 'video', 'title', 'description']


class SubjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"

class StudentquerySerializers(serializers.ModelSerializer):

    class Meta:
        model = StudentQuery
        fields = "__all__"      

class ContactSerializers(serializers.ModelSerializer):   
     
    class Meta:
        model = Contact
        fields = "__all__"   


