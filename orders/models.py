from django.db import models
from customers.models import ExtendUser, AbstractUser
from products.models import Products


class Orders(models.Model):
    customer_id = models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
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
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0) #criar metodo para totalizar com a qtd.
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y - %H:%M')

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y - %H:%M')

    class Meta:
        verbose_name_plural = 'Order_Products'
