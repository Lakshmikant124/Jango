from django.shortcuts import render 
from django.http import HttpResponse 


def home(request):
    return HttpResponse("Welcome to first project")
def demo(request):
    return HttpResponse("Welcome to demo page")