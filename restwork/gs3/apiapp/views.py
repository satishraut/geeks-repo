from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        serializer = JSONRenderer().render(serializer.data, many=True)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)

        if serializer.is_valid():
            print(serializer)
            serializer.save()
            res = {'msg':'Data Created Succussfully...'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'PUT':
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
    if request.method == 'DELETE':
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