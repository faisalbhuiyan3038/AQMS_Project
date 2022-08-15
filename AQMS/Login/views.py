from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def HomePage_view(request):
    return render(request, "Login/HomePage.html")

def simple_view(request):
    return HttpResponse("What's Up")

