from django.shortcuts import render
from purbeurre.products.models import Product
from django.http.response import JsonResponse


def get_all_products(request):
    # TODO
    product = Product.objects.all()
    product = list([product.name for product in product])
    return JsonResponse(product, safe=False)
