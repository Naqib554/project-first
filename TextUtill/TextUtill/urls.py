# Urls.py
"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .import views

# Code for video 6
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#
# ]

# Code for video 7
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup_page,name='signup_page'),
    path('login/', views.login_page, name='log'),
    path('otp-login/', views.otp_login, name='otp_login'),
    path('home/',views.homepage,name='home'),
    path('logout/',views.logoutpage,name='logout'),
    path('analyze', views.analyze, name='analyze'),
    # path('ex1', views.ex1, name='ex1'),
    path('about_view/', views.about_view, name='about_view'),
    path('contact',views.contact,name='contact'),


]
