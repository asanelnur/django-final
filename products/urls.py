from django.urls import path

from products import views

app_name = "products"

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/category/<int:category_id>', views.products, name='category'),
    path('baskets/', views.basket, name='basket'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('order/add/<int:product_id>/', views.order_add, name='order_add'),
    path('order/', views.order, name='order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('old-order/', views.old_order, name='old_order'),
    path('order-created/', views.order_created, name='order_created'),
    # path('payment/<int:order_id>', views.payment, name='payment'),
    path('orderitem/delete/<int:orderitem_id>/', views.orderitem_remove, name='orderitem_remove'),
    path('orderitem/quantity/minus/<int:orderitem_id>/', views.orderitem_quantity_minus, name='orderitem_quantity_minus'),
    path('orderitem/quantity/plus/<int:orderitem_id>/', views.orderitem_quantity_plus, name='orderitem_quantity_plus'),
]
