from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('hello world')

def calculate(request):
    return HttpResponse('hello world Two')
    # return HttpResponse( 'sum : ', 5 + 10)

