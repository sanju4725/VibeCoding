from django.shortcuts import render
from django.http import HttpResponse

def user_home(request):
    return HttpResponse("<h1>Hey, this is the user page</h1>")

def profile(request):
    return HttpResponse("<h1>This is the profile page</h1>")

def login_view(request):
    return HttpResponse("<h1>This is the login page</h1>")