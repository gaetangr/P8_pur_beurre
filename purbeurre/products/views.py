from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from purbeurre.products.models import Product
from purbeurre.users.models import Favorite


class ProductListView(ListView):
    """Simple view that lists all the Products on a single page
    Args:
        ListView : Render some list of objects,
        set by self.model or self.queryset. self.queryset
        can actually be any iterable of items, not just a queryset.
    """

    paginate_by = 10
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().filter(name="Nutella")
        return context


class ProductDetailView(DetailView):
    """Detail view that lists display information for a given <Model> on a single page
    Args:
        DetailView : Render a "detail" view of an object.
    """

    model = Product


def save_favorite(request, id):
    user = request.user
    product = Product.objects.get(pk=id)
    Favorite.objects.create(product=product, substitute=product, user=user)
    messages = _("Your substitue has been save !")
    return redirect("users:detail", user)


def get_all_products(request):
    # TODO: Recherche par prdouit, recupérer le term, term = request.get, pas object all #product object filter

    product = Product.objects.all()
    product = list([product.name for product in product])
    return JsonResponse(product, safe=False)
