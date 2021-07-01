from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
def home(request):
    r = requests.get('https://tryingtoupload123.herokuapp.com/api/')
    # r = dict(r)
    # print(r.json())
    r = r.json()
    # for i in r:
    #     print(i['id'])
    #     print(i['title'])
    #     print(i['images'])
    return render(request,'end/main.html',{'find':r})