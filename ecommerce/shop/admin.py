from django.contrib import admin
from .models import Product, Category, Cart, CartItem, Order, OrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)