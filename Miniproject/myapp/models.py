from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
class MenuItem (models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='menu_items')
    Dishname =models.CharField(max_length=255)
    Description=models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    image=models.ImageField(upload_to='dishimage')
    category=models.CharField(max_length=100)
    rating=models.FloatField(default=0.0)
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
class Cartitem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
class Order(models.Model):
    STATUS_CHOICES = [
    ('received', 'Order Received'),
    ('preparing', 'Preparing'),
    ('out_for_delivery', 'Out for Delivery'),
    ('delivered', 'Delivered'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='received')
    payment_id = models.CharField(max_length=100, blank=True, null=True)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE,related_name='items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


