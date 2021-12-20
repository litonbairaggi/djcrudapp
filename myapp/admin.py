from django.contrib import admin
from .models import UserModel

# Register your models here.

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'department', 'gender', 'address', 'language']

# admin.site.register(UserModel)