# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Captcha
# # import django form
from django import forms
# import user model from django
from django.contrib.auth.models import User

# django set password
from django.contrib.auth.forms import SetPasswordForm


# class Userform(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username","email","password1","password2")

    
class CaptchForm(forms.Form):
    captcha = CaptchaField()

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model= User
        fields = ['new_passord1', 'new_password2']



  