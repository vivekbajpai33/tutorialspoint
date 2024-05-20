"""
URL configuration for english_grammar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import home
from authentication.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('authentication.urls')),
    path('', home),
    path('about/', about, name='about'),
    path('edit-profile/<int:id>/', profile_edit, name='profile-edit'),
    path('courses/', Courses, name='courses'),
    path('our-courses/', include('home.urls')),
    path('captcha/', include('captcha.urls')),
    path('api-auth/', include('rest_framework.urls')),
]




if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 



