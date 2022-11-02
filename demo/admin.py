from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display=['email','password']
    search_fields=['email','password']