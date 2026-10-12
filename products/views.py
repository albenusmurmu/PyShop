from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

def calculate(request):
    return HttpResponse('hello world Two')
#     # return HttpResponse( 'sum : ', 5 + 10)

