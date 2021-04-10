from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y - %H:%M')

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y - %H:%M')

    class Meta:
        verbose_name_plural = 'Products'

