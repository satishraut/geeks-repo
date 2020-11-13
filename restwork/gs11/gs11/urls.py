
from django.contrib import admin
from django.urls import path
from apiapp.views import StudentList,StudentCreate,StudentRetrive,StudentUpdate, StudentDestroy



urlpatterns = [
    path('admin/', admin.site.urls),
    path('studapi/',StudentList.as_view()),
    #path('studapi/',StudentCreate.as_view()),
    #path('studapi/<int:pk>',StudentUpdate.as_view()),
    #path('studapi/<int:pk>',StudentUpdate.as_view()),
    path('studapi/<int:pk>',StudentDestroy.as_view()),
]
