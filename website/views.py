from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,"home.html")


def page1(request):
    return HttpResponse("<h1>This is Page 1</h1>")