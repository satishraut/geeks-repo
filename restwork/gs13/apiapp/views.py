from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView, 
    DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView)

# class StudentListView(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer

# class StudentLCreateView(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer

# class StudentLRetriveView(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer

# class StudentUpdateView(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer


# class StudentDestroyView(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetriveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetriveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrivUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
