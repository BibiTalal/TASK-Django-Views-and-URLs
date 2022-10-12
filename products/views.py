from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product


def get_home(request):
    return HttpResponse("<h1> Welcome</h1>")


def get_product(request, product_id):
    products = Product.objects.get(id=product_id)
    return HttpResponse(
        f"Name: {products.name}, Price: {products.price}, Description: {products.description} "
    )
