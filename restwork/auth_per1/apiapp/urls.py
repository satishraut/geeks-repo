from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentAPIViewSet

router = DefaultRouter()
router.register('student',StudentAPIViewSet,basename='student')
