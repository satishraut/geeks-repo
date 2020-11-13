from django.contrib import admin
from django.urls import path
from apiapp.views import(StudentListCreateView,StudentRetriveUpdate,StudentRetriveDestroy,
StudentRetrivUpdateDestroy)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('studapi/',StudentLCreateView.as_view()),
    #path('studapi/<int:pk>',StudentRetriveUpdateDestroy.as_view()),
    #path('studapi/<int:pk>',StudentLRetriveView.as_view()),
    #path('studapi/<int:pk>',StudentUpdateView.as_view()),
    #path('studapi/<int:pk>',StudentUpdateView.as_view()),
    #path('studapi/<int:pk>',StudentDestroyView.as_view())
    path('studapi/',StudentListCreateView.as_view()),
    #path('studapi/<int:pk>',StudentRetriveUpdate.as_view()),
    #path('studapi/<int:pk>',StudentRetriveDestroy.as_view()),
    path('studapi/<int:pk>',StudentRetrivUpdateDestroy.as_view()),

]
