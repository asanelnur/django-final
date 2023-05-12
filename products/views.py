from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.pagination import PageNumberPagination

from products import forms

from products.models import Dish, Category, Basket, Order, Payment, OrderItem


# Create your views here.



def products(request):
    context = {
        'title': 'Restaurant',
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
        Basket.objects.create(user=request.user, products=product)
    else:
        print("Basket already exits")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'title': 'storeApp',
        'baskets': baskets
    }
    return render(request, 'products/basket.html', context)


@login_required
def order_add(request, product_id):
    product = Dish.objects.get(id=product_id)
    print(product.name)
    try:
        order = Order.objects.filter(user=request.user, status=False).first()
    except:
        order = None
    try:
        orderitem = OrderItem.objects.get(order_id=order.id, dish_id=product.id)
    except:
        orderitem=None

    if not order:
        payment = Payment.objects.create()
        order = Order.objects.create(user=request.user, payment=payment, place_number=0)
        payment.total += product.price
        payment.save()
        order_item = OrderItem.objects.create(dish=product, order=order)
        order_item.quantity += 1
        order_item.save()
    elif not orderitem:
        order_item = OrderItem.objects.create(dish=product, order=order)
        order_item.quantity += 1
        order_item.save()

        order.payment.total += product.price
        order.payment.save()
    else:
        orderitem.quantity += 1
        orderitem.save()
        order.payment.total += product.price
        order.payment.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])






@login_required
def order(request):
    # order = Order.objects.get(user=request.user)
    try:
        order = Order.objects.get(user=request.user, status=False)
        print(order)
    except:
        payment = Payment.objects.create()
        order = Order.objects.create(user=request.user, payment=payment, place_number=0)
        context = {
            'title': 'storeApp',
            'order': order,
            'total': 0
        }
        return render(request, 'products/order.html', context)
    if request.method == 'POST':
        # print(request.POST['payment_type'])
        form = forms.PaymentType(data=request.POST)
        if form.is_valid():
            order = Order.objects.get(id=order.id)
            order.payment.status = True
            order.payment.type = request.POST['payment_type']
            order.place_number = request.POST['place_number']
            order.save()
            order.payment.save()
            return HttpResponseRedirect(reverse('products:order'))
    else:
        form = forms.PaymentType()

    orderitems = OrderItem.objects.filter(order=order)
    # if not orderitems.exists():
    #     order.delete()
    #     return render(request, 'products/order.html')
    total = 0
    for orderitem in orderitems:
        total += orderitem.quantity*orderitem.dish.price

    context = {
        'title': 'storeApp',
        'order': order,
        'total': total,
        'orderitems': orderitems,
        'form': form,
    }
    return render(request, 'products/order.html', context)
# @login_required
# def order(request):
#     try:
#         order = Order.objects.get(user=request.user, user__order__status=False)
#     except:
#         order=None
#     if not order:
#         return render(request, 'products/order.html')
#     orderitems = OrderItem.objects.filter(order=order)
#     total = 0
#     for orderitem in orderitems:
#         total += orderitem.quantity*orderitem.dish.price
#
#     context = {
#         'title': 'storeApp',
#         'order': order,
#         'total': total,
#         'orderitems': orderitems
#     }
#     return render(request, 'products/order.html', context)



@login_required
def orderitem_remove(request, orderitem_id):
    orderitem = OrderItem.objects.get(id=orderitem_id)
    orderitem.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def orderitem_quantity_minus(request, orderitem_id):
    orderitem = OrderItem.objects.get(id=orderitem_id)
    if orderitem.quantity>1:
        orderitem.quantity -= 1
        orderitem.save()
    else:
        orderitem.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def orderitem_quantity_plus(request, orderitem_id):
    orderitem = OrderItem.objects.get(id=orderitem_id)
    orderitem.quantity += 1
    orderitem.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# @login_required
# def payment(request, order_id):
#     if request.method == 'POST':
#         print(request.POST['payment_type'])
#         form = forms.PaymentType(data=request.POST)
#         if form.is_valid():
#             order = Order.objects.get(id=order_id)
#             order.payment.status = True
#             order.payment.type = request.POST['payment_type']
#             order.payment.save()
#             return HttpResponseRedirect(reverse('products:order'))
#     else:
#         form = forms.PaymentType()
#     context = {
#         'form': form,
#         'order_id': order_id
#     }
#     return render(request, 'products/order-create.html', context)


@login_required
def order_created(request):
    order = Order.objects.get(user=request.user, status=False)
    order.status=True
    order.save()
    orderitems = OrderItem.objects.filter(order=order)
    total = 0
    for orderitem in orderitems:
        total += orderitem.quantity * orderitem.dish.price

    context = {
        'title': 'storeApp',
        'order': order,
        'total': total,
        'orderitems': orderitems
    }
    return render(request, 'products/order-create-succes.html', context)





@login_required
def old_order(request):
    try:
        orders = Order.objects.filter(user=request.user, status=True)
    except:
        return render(request, 'products/order.html')

    paginator = Paginator(orders, 2)
    page_number = request.GET.get("page")
    page_order = paginator.get_page(page_number)
    context = {
        'title': 'storeApp',
        'page_order': page_order,
    }
    return render(request, 'products/old-order.html', context)


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    print(order)

    orderitems = OrderItem.objects.filter(order=order)
    total = 0
    for orderitem in orderitems:
        total += orderitem.quantity * orderitem.dish.price

    context = {
        'title': 'storeApp',
        'order': order,
        'total': total,
        'orderitems': orderitems
    }
    return render(request, 'products/orderdetail.html', context)