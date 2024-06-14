from django import forms
from .models import BlogStory


class Blogform(forms.ModelForm):
    class Meta:
        model = BlogStory
        fields = ['title', 'story', 'description', 'story_pic']
