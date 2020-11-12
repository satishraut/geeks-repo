
from django.contrib import admin
from django.urls import path
from apiapp.views import StudentAPIView

from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studapi/',StudentAPIView.as_view()),
    path('studapi/<int:pk>',StudentAPIView.as_view()),
]
