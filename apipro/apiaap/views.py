from django.shortcuts import render
from rest_framework import viewsets
from .models import imagestore
from .serializers import imagestoreSerializer
from rest_framework.views import APIView 
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# @api_view(['GET', 'POST'])
# @csrf_exempt
# def upload_it(request):
#     if request.method == 'GET':
#         info = imagestore.objects.all()
#         serializer = imagestoreSerializer(info,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = imagestoreSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         else:
#             return JsonResponse(serializer.errors,status=400)

class upload_it(APIView):
    def post(self,request):
        serializer = imagestoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message":"done"})
        return JsonResponse(serializer.errors)
    
    def get(self,request):
        data = imagestore.objects.all()
        serializer = imagestoreSerializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)