from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, "frontend/index.html", context=context)


# def getCategories(request):
#     categories = Category.objects.all()
#
#     context = {
#         'categories': categories
#     }
#
#     return render(request, 'frontend/index.html', context=context)

def getProductDetails(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }

    return render(request, "frontend/product_details.html", context=context)
