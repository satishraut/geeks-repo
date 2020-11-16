
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import exception_handler
from django.http import JsonResponse
from rest_framework.exceptions import APIException
from django.http import JsonResponse
from rest_framework.status import HTTP_403_FORBIDDEN



def custom_exception(exc, context):
    # Call REST framework's default exception handler first, 
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
        #error_data= some custom error messaging'
    # #return JsonResponse(error_data,safe=False, status=403)
    #     exc.detail = 'You do not have authorised user'
    return response


