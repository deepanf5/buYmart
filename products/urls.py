from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='updateItem'),
    path('view/', views.view, name='view'),





]


