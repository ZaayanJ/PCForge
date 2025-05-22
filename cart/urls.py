from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name="shoppingcart"),
    path('add/', views.cart_add, name="cart_add"),
    # path('delete/', views.cart_delete, name="cart_delete"),
    # path('update/', views.cart_update, name="cart_update"),
    path('checkout/', views.checkout, name="checkout"),
    path('order/', views.process_order, name="process_order"),
    path('cart/add-bulk/', views.cart_add_bulk, name='cart_add_bulk'),
]