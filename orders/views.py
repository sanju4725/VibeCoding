from django.shortcuts import render
from django.http import HttpResponse

def orders_home(request):
    return HttpResponse("<h1>Hey, this is the orders page</h1>")

def checkout(request):
    return HttpResponse("<h1>This is the checkout page</h1>")