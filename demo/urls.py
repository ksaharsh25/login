
from django.urls import path
# from django.contrib.auth import *
from demo.views import *
from demo.models import * 

urlpatterns=[
    path('http',http,name="http"),
    path('mob',mobile,name="mobile"),
    path('verify',verify,name="verify"),
]