from django.db import models
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class Captcha(models.Model):
    captcha = CaptchaField()

    def __str__():
        return Captcha





