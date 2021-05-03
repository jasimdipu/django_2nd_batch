from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product-details/<str:pk>', views.getProductDetails, name='product_details')
]
