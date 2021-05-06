"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views as local_views

urlpatterns = [  
    # Регистрация и активация аккаунта
    path('signup/', local_views.UserRegisterFormView.as_view(),\
    name="signup_user"),
    path('need-activate/', local_views.UserRegisterFormView.need_activate_page),
    path('activate/<uidb64>/<token>/', local_views.UserRegisterFormView\
        .activate_account, name='activate_account'),

    # Профиль юзера
    path('profile/', login_required(local_views.UserDetailView.as_view()),\
        name='profile'),

    # Вход/выход
    path('login/', auth_views.LoginView\
        .as_view(redirect_authenticated_user=True,\
        template_name='accounts/login.html'), name='login'),
    path('logout/', login_required(auth_views.LogoutView\
        .as_view(template_name='accounts/logged_out.html')), name='logout'),

    # Смена пароля
    path('password_change/', auth_views.PasswordChangeView\
        .as_view(template_name='accounts/password_change_form.html'),\
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView\
        .as_view(template_name='accounts/password_change_done.html'),\
        name='password_change_done'),
    
    # Сброс пароля
    # Можно изменить шаблон письма - email_template_name
    path('password_reset/', auth_views.PasswordResetView\
        .as_view(template_name='accounts/password_reset_form.html',\
        email_template_name='accounts/password_reset_email.html'),\
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView\
        .as_view(template_name='accounts/password_reset_done.html'),\
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView\
        .as_view(template_name='accounts/password_reset_confirm.html'),\
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView\
        .as_view(template_name='accounts/password_reset_complete.html'),\
        name='password_reset_complete'),
]