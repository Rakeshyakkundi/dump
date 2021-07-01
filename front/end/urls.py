from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from end import views

urlpatterns = [
    path('', views.home),
]

