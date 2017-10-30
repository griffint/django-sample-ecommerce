from django.db import models
from django.contrib.auth import models as auth_models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    # limit price of single product to $999,999.00
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Cart(models.Model):
    # limit price of a cart to $999,999,999.00 - sorry billionaires!
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    # carts can have many products, a product can be in many carts
    # so a many-to-many field is needed
    products = models.ManyToManyField(Product)
    # use default auth users to link to carts
    customer = models.OneToOneField(auth_models.User)


class Order(models.Model):
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    products = models.ManyToManyField(Product)
    # any user can have multiple orders, so many to one relationship
    customer = models.ForeignKey(auth_models.User)
    order_placed_time = models.DateTimeField()
    address = models.CharField(max_length=300)
