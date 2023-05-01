from django.urls import path

from products import views

app_name = "products"

urlpatterns = [
    path('', views.index),
    path('products/', views.products, name='products'),
    path('products/category/<int:category_id>', views.products, name='category'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('order/add/<int:product_id>/', views.order_add, name='order_add'),
]
