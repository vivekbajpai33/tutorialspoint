from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import courses





class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


class CoursesSerializers(serializers.ModelSerializer):

    subjectname_obj = serializers.SerializerMethodField("get_subjectname_obj")

    def get_subjectname_obj(self, obj):
        return obj.subjectname.subject_name
    

    class Meta: 
        model = courses
        fields = ['subjectname_obj','title','description','paid']


class AddCoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = courses
        fields= "__all__"
    

    


        
