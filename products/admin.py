from django.contrib import admin
from .models import Product, Offer


# create a model to show in table form what actually will show header with data
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
    list_filter = ('discount',)
    search_fields = ('code',)
    list_per_page = 20
    list_editable = ('discount',)

# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)