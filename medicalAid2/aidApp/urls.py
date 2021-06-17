from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(' ', views.home, name="home"),
    path("register/", views.register, name='register'),
    path("user_login/", views.user_login, name='user_login'),
    path("user_logout/", views.user_logout, name="user_logout"),




    # reset password urls
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),



]
