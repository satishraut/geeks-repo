from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self,request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()

        serializer = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created Succussfully...'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self, request,*args, **kwargs):
        json_data = request.body
        #print(json_data)
        stream=io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        #print(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated...'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/data')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def delete(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData=JSONParser().parse(stream)
        id = pythonData.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted!!!'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/data')
        return JsonResponse(res,safe=True)
