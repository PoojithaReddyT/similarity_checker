from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from users import views
from . import main

urlpatterns=[

    url(r'^$',views.add,name='home'),
    url(r'about/$',views.about,name='about'),
    url(r'file2/$',views.add2,name='add2'),
    url(r'file2/result/$',main.percent,name='getresult'),
    #path('', views.add, name='home'),
]
