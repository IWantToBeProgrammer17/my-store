from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def secondpage(request):
    return HttpResponse("Hello, Ini Halaman Kedua Saya.")
    
    