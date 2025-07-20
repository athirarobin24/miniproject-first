from django.contrib import admin
from .models import Restaurant, MenuItem, Cart, Cartitem, Order, OrderItem, Wishlist, Review


# Register your models here.
admin .site.register(Restaurant)
admin .site.register(MenuItem)
admin .site.register(Cart)
admin .site.register(Cartitem)
admin .site.register(Order)
admin .site.register(OrderItem)
admin .site.register(Wishlist)
admin .site.register(Review)