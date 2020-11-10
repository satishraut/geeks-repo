from django.contrib import admin
from .models import Profile, Post


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','mob']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']