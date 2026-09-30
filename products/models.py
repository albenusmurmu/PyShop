from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField(max_length=255)
    discount = models.FloatField()

# Test case
    # def __str__(self):
    #     return self.name
    # class Meta:
    #     db_table = 'product'
    #     verbose_name_plural = 'products'
    #     ordering = ['name']
