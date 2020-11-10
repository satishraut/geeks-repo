
from django.contrib import admin
from django.urls import path
from apiapp.views import student_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studapi/',student_api),
    path('studapi/<int:pk>',student_api),
]
