from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'myapp/home.html')


def another(request):
    return render(request, 'myapp/about.html')
