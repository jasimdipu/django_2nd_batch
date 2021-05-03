from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    search_fields = ['name', 'phone', 'email', ]
    list_filter = ['created_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'tag']
    list_filter = ['category', 'price', 'tag']
    filter_horizontal = ['tag']


class OrderAdmin(admin.ModelAdmin):
    # list_display = ['customer', 'product', 'order_date', 'status']
    search_fields = ['customer']
    list_filter = ['order_date', 'status']
    filter_horizontal = ['customer', 'product']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
