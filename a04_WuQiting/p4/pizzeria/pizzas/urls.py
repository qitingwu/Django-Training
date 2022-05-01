"""Defines URL patterns for pizzas."""
from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for Pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Toppings for the chosen pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]