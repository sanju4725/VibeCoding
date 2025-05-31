from django.shortcuts import render
from django.http import HttpResponse

def products_home(request):
    return HttpResponse("<h1>Hey, this is the products page</h1>")