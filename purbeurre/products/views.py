from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from purbeurre.products.forms import ProductSearchForm
from purbeurre.products.models import Category, Product
from purbeurre.users.models import Favorite


class ProductListView(ListView):
    """Simple view that lists all the Products on a single page
    Args:
        ListView : Render some list of objects, set by self.model or self.queryset
        self.queryset can actually be any iterable of items, not just a queryset.
    """

    paginate_by = 10
    model = Product


def search_product(request, product_name):
    # form = ProductSearchForm(request.POST)
    product_name = Product.objects.filter(name=product_name)[0]
    cat_pk = product_name.categories.all()[0].pk
    cat = Category.objects.get(pk=cat_pk)
    cat = cat.categories.all().order_by("nutriscore_grade")
    context = {"product": cat}
    return render(request, "products/product.html", context)


def search(request):
    form = ProductSearchForm(request.POST)
    if request.method == "POST":
        # data = request.POST.get("name")
        pass
    context = {"form": form}
    return render(request, "pages/intro.html", context)


class ProductDetailView(DetailView):
    """Detail view that lists display information for a given <Model> on a single page
    Args:
        DetailView : Render a "detail" view of an object.
    """

    model = Product


def save_favorite(request, id_product):
    """Save a substitue for a product and redirct user to
    the favoris view

    Args:
        id_product (int): Id of the product to be saved
    """
    user = request.user
    product = Product.objects.get(pk=id_product)
    Favorite.objects.create(product=product, substitute=product, user=user)
    return redirect("users:fav", user)


def get_all_products(request):
    # TODO: Recherche par prdouit, recupérer le term, term = request.get, pas object all #product object filter

    product = Product.objects.all()
    product = list([product.name for product in product])
    return JsonResponse(product, safe=False)
