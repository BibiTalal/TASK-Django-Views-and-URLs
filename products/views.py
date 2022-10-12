from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def get_home(request):
    return HttpResponse("<h1> Welcome</h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": {
            "name": product.name,
            "description": product.description,
            "price": product.price,
        }
    }
    return render(request, "product_detail.html", context)
