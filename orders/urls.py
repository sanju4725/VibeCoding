from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_home, name='orders_home'),
    path('', views.checkout, name='checkout'),
]