"""Messenger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as authViews
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path("login/", views.user_login, name='login'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path('registration/', views.user_registration, name='registration'),
    path('messanger/', views.messenger,name='messanger'),
    path('create_room', views.create_room, name="create_room"),
    path(r'chat/<int:room_id>', views.chat, name='chat'),


]
