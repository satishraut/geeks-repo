from django.contrib import admin
from .models import Job, Subscriber, Subscription
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['company','company_email','title','details','status','date_created','date_modified']

@admin.register(Subscriber)
class JobAdmin(admin.ModelAdmin):
    list_display=['email','date_created','date_modified']

@admin.register(Subscription)
class JobAdmin(admin.ModelAdmin):
    list_display=['email','user','job','date_created','date_modified']