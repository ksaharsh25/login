from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth import *
from demo.views import *

urlpatterns=[
    path('',login,name="login"),
]