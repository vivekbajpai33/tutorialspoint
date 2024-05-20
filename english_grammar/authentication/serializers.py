from rest_framework import serializers
from django.contrib.auth.models import User




class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
