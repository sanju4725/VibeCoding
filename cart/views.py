from django.shortcuts import render
from django.http import HttpResponse

def cart_home(request):
    return HttpResponse("<h1>Hey, this is the cart page</h1>")

def view_cart(request):
    return HttpResponse("<h1>This is the cart page</h1>")