"""squirrel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
import csv
import datetime
import os
from .models import biaoge

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main),
    path('map/',views.map),
    #path('add/',views.add),
    path('stats/<str:squirrel_id>/', views.status),
    path('stats/<str:squirrel_id>/edit/', views.edit),
    path('add/',views.add),
]
