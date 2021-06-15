from django.shortcuts import render
from django.http import HttpResponse
#Create your views 

def index(request):
    return HttpResponse("Hello World!")