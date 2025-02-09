from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def landingpage(request):
    #return HttpResponse("Hello, Ini Halaman Saya.")
    #return HttpResponse("<i><h2>Hello, Ini Halaman Saya.</h2></i> </p> line ke dua")
    #return HttpResponse("<h2>Hello, Ini Halaman Saya.</h2> </p> line ke dua <p> <img src='https://pintu-academy.pintukripto.com/wp-content/uploads/2021/06/Bitcoin-Bubble.png' > " )
    return HttpResponse("<h2 style='color:blue;'>Hello, Ini Halaman Saya.</h2> <p style='color:red;'> line ke dua <p> <img src='https://www.w3schools.com/html/pic_trulli.jpg' > " )