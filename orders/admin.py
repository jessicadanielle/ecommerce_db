from django.contrib import admin
from .models import Product, Customer, Order, Shipment, Cart, Payment

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Shipment)
admin.site.register(Cart)
admin.site.register(Payment)
