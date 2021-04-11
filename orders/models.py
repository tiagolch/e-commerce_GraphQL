from django.db import models
from customers.models import User
from products.models import Products


class Orders(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer_id)

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y - %H:%M')

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y - %H:%M')

    class Meta:
        verbose_name_plural = 'Orders'


class Order_products(models.Model):
    product = models.ForeignKey(Products, related_name='products', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y - %H:%M')

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y - %H:%M')

    class Meta:
        verbose_name_plural = 'Order_Products'
