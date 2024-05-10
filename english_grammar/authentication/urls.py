from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Login, name='login'),
    path('sign-up/', signup, name='login'),
    path('logout/', Logout, name='logout')
]