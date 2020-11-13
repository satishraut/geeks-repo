from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (
    ListCreateAPIView,RetrieveUpdateDestroyAPIView)

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrivUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
