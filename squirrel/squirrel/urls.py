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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles, admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.good),
    path('map/',views.map),
    #path('add/',views.add),
    path('status/<str:squirrel_id>/', views.goodview),
    path('status/<str:squirrel_id>/edit/', views.goodedit),
    path('add/',views.goodadd),
    path('success/',views.success),
    re_path(r'^search/$', views.search, name='search'),
    path('overall/',views.overall),
    path('stats/',views.stats)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
