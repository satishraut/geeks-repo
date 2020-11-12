from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello world'})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is post request'})

# @api_view(['POST','GET'])
# def hello_world(request):
#     if request.method=="GET":
#         return Response({'msg':'This is get request..'})
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is post request','data':request.data})


class StudentAPIView(APIView):
        def get(self,request, pk=None, format=None):
            id = pk
            if id is not None:
                try:
                    stu = Student.objects.get(id=id)
                    serializer = StudentSerializer(stu)
                    return Response(serializer.data)
                except:
                    return Response('Student is not present')
            stu = Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
           
        def post(self,request,format=None):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Inserted Succusefully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        def put(self, request, pk, format=None):
            id = pk
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data=request.data,partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data Updated....'})
            return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def patch(self, request, pk, format=None):
            id = pk
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data Updated....'})
            return Reponse(serializer.errors)

        def delete(self, request, pk, patch):
            id = pk
            stu = Student.objects.get(pk=id)
            stu.delete()
            return Response({'msg':'Data Deleted..'},status=status.HTTP_202_ACCEPTED)

        