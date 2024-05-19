from django.urls import path
from .views import *
# forgot password
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', Login, name='login'),
    path('sign-up/', signup, name='sign-up'),
    path('logout/', Logout, name='logout'),
    path('reset-password/', ResetPassword, name='password-reset'),
    path('change-password/', ChangePassword, name='change-password'),

    # reset password url
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_rest/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView)
]