from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2000)


    # def __str__(self):
    #     return self.name
    # class Meta:
    #     db_table = 'product'
    #     verbose_name_plural = 'products'
    #     ordering = ['name']
