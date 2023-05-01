from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import Dish, Category, Basket, Order, Payment, OrderItem


# Create your views here.

def index(request):
    context = {
        'title': 'Store',
        'username': 'Asan Elnur',
        'is_promotion': False
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'storeApp',
        'products': Dish.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'products/products.html', context)


def products(request, category_id=None):
    if category_id:
        category = Category.objects.get(id=category_id)
        products = Dish.objects.filter(category=category)
    else:
        products = Dish.objects.all()

    context = {
        'title': 'products',
        'products': products,
        'categories': Category.objects.all(),
    }
    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Dish.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def order_add(request, product_id):
    product = Dish.objects.get(id=product_id)
    print(product.name)
    try:
        order = Order.objects.get(user_id=request.user.id)
    except:
        order = None
    try:
        orderitem = OrderItem.objects.get(order_id=order.id, dish_id=product.id)
    except:
        orderitem=None

    if not order:
        payment = Payment.objects.create()
        order = Order.objects.create(user=request.user, payment=payment, place_number=0)
        order.total += product.price
        payment.total = order.total
        payment.save()
        order.save()
        order_item = OrderItem.objects.create(dish=product, order=order)
        order_item.quantity += 1
        order_item.save()
    elif not orderitem:
        order_item = OrderItem.objects.create(dish=product, order=order)
        order_item.quantity += 1
        order_item.save()

        order.total += product.price
        order.payment.total = order.total
        order.payment.save()
        order.save()
    else:
        orderitem.quantity += 1
        orderitem.save()
        order.total += product.price
        order.payment.total = order.total
        order.payment.save()
        order.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def order_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])