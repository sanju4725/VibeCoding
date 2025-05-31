from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
]