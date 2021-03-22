from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello Skill jobs django batch 2</h2>\n<h4>This is our first django project</h4>")


def about_us(request):
    return HttpResponse("<h1>About us</h2>\n<h4>We are successfully building another page</h4>")
