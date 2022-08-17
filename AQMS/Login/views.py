from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginPage_view(request):
    return HttpResponse('hello')