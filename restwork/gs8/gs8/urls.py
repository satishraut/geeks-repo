
from django.contrib import admin
from django.urls import path
from apiapp.views import student_api

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('studapi/', hello_world),
    path('studapi/',student_api)
]
