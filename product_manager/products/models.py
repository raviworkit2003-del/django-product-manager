from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class client(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_join=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name