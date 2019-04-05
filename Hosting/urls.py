"""Hosting URL Configuration

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
import sys
sys.path.append('../')
import FR.main as main
import FR.FacialRecognition as Fr
urlpatterns = [
    path('admin/', admin.site.urls),
    path("/", main.index, name="index"),
    path("", main.index, name="index"),
    path("AuthUser/", main.AuthUser, name="AuthUser"),
    path("upImage/", main.UpImage, name="UpImage"),
    path("Demo/", main.Demo, name="Demo"),
    path("AuthenticateUser/", Fr.AuthenticateUser, name="AuthenticateUser"),
    path("Clients/", main.Clients, name="AuthenticateUser")
]
