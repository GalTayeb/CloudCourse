from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('orders/', views.orders),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('orders/add_item_to_cart/<int:product_id>/', views.add_item_to_cart),
    path('cart/delete_item_from_cart/<int:product_id>/', views.delete_item_from_cart),
    path('add_product/', views.add_product),
    path('delete_product/<int:product_id>/', views.delete_product),
]
