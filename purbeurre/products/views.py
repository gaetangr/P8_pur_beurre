from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from purbeurre.products.models import Product, Category
from purbeurre.users.models import Favorite
from purbeurre.products.forms import ProductSearchForm


def search_product(request, product_name):
    form = ProductSearchForm(request.POST)
    product_name = Product.objects.filter(name=product_name)[0]
    cat_pk = product_name.categories.all()[0].pk
    cat = Category.objects.get(pk=cat_pk)
    cat = cat.categories.all().order_by("nutriscore_grade")
    context = {"product": cat}
    return render(request, "products/product.html", context)


def search(request):
    form = ProductSearchForm(request.POST)
    if request.method == "POST":
        data = request.POST.get("name")
    context = {"form": form}
    return render(request, "pages/intro.html", context)


class ProductDetailView(DetailView):
    """Detail view that lists display information for a given <Model> on a single page
    Args:
        DetailView : Render a "detail" view of an object.
    """

    model = Product


def save_favorite(request, id_product, id_favoris):
    user = request.user
    product = Product.objects.get(pk=id_product)
    Favorite.objects.create(product=product, substitute=product, user=user)
    messages = _("Your substitue has been save !")
    return redirect("users:detail", user)


def get_all_products(request):
    # TODO: Recherche par prdouit, recupérer le term, term = request.get, pas object all #product object filter

    product = Product.objects.all()
    product = list([product.name for product in product])
    return JsonResponse(product, safe=False)
