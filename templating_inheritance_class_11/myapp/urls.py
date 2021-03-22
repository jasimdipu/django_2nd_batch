from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='myapp'),
    path("about", views.another, name='about')
]