from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    shipment_date = models.DateField()
    shipment_quantity = models.IntegerField()

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField()

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=100)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
