from django.urls import path, include
from .views import *
# forgot password
from django.contrib.auth import views as auth_views

# set api path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', UserApiView),



urlpatterns = [
    path('login/', Login, name='login'),
    path('sign-up/', signup, name='sign-up'),
    path('logout/', Logout, name='logout'),
    path('reset-password/', ResetPassword, name='password-reset'),
    path('change-password/', ChangePassword, name='change-password'),
    path('', include(router.urls)),
    path(r'courses/api/', CoursesApiView.as_view(), name='addcourses'),
    path(r'edit-courses/<int:pk>/', EditCoursesApiView.as_view(), name='edit_courses'),
    path(r'add-courses/', AddCoursesView.as_view(), name='add_courses'),
    path(r'delete/<int:pk>/', DeleteCoursesApi.as_view(), name='delete_courses'),
    # path(r'user/', UserApiView.as_view(), name="user-api"),
    # reset password url
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_rest_done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]