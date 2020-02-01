from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import *


# Create your views here.
def index(request):
    products = Product.objects.all().order_by("name")
    return render(request, 'main/index.html', {
        "products": products
    })


@csrf_exempt
def add_product(request):
    name = request.POST["name"]
    price = request.POST["price"]
    availableitems = request.POST["availableitems"]
    Product.objects.create(name=name, price=price, availableItems=availableitems)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_product(request, product_id):
    Product.objects.get(id=product_id).delete()
    return HttpResponseRedirect("/")


def orders(request):
    products = Product.objects.all().order_by("name")
    order_history = Order.objects.all().filter(status=True)
    return render(request, 'main/orders.html', {
        "products": products,
        "order_history": order_history
    })


def cart(request):
    total = 0
    if Order.objects.all().filter(status=False):
        current_order = Order.objects.get(status=False)
        current_cart = current_order.listOfProducts.all()
        for product in current_order.listOfProducts.all():
            total += product.price
        return render(request, 'main/cart.html', {
            "current_cart": current_cart,
            "total": total
        })
    else:
        return render(request, 'main/nocart.html')


@csrf_exempt
def checkout(request):
    current_order = Order.objects.get(status=False)
    current_cart = current_order.listOfProducts.all()
    for product in current_cart:
        product.availableItems = product.availableItems - 1
        product.save()
    current_order.status = True
    current_order.save()
    return HttpResponseRedirect("/")


@csrf_exempt
def add_item_to_cart(request, product_id):
    if Order.objects.all().filter(status=False):
        current_order = Order.objects.get(status=False)
    else:
        current_order = Order.objects.create(date=timezone.now(), status=False)
    product = Product.objects.get(id=product_id)
    current_order.listOfProducts.add(product)
    return HttpResponseRedirect("/cart")


@csrf_exempt
def delete_item_from_cart(request, product_id):
    current_order = Order.objects.get(status=False)
    product = Product.objects.get(id=product_id)
    current_order.listOfProducts.remove(product)
    return HttpResponseRedirect("/cart")
