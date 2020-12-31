from django.shortcuts import render, redirect
from purbeurre.products.models import Product
from purbeurre.users.models import Favorite, User
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class ProductListView(ListView):
    """Simple view that lists all the Products on a single page
    Args:
        ListView : Render some list of objects, set by self.model or self.queryset. self.queryset can actually be any iterable of items, not just a queryset.
    """

    paginate_by = 10
    model = Product


class ProductDetailView(DetailView):
    """Detail view that lists display information for a given <Model> on a single page
    Args:
        DetailView : Render a "detail" view of an object.
    """

    model = Product


def save_favorite(request):
    user = User.objects.get(pk=1)
    product = Product.objects.get(pk=22)
    Favorite.objects.create(product=product, substitute=product, user=user)
    return redirect("/")


def get_all_products(request):
    # TODO
    product = Product.objects.all()
    product = list([product.name for product in product])
    return JsonResponse(product, safe=False)
