from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    category = models.OneToOneField(Category, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    tag = models.ManyToManyField(to=Tag, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Out of delivery', 'Out of delivery'),
    )
    customer = models.ManyToManyField(Customer, blank=True)
    product = models.ManyToManyField(Product, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
