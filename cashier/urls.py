from django.urls import path

from . import views

urlpatterns = [
    path("", views.secondpage, name="index"),
]