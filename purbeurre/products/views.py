from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView
from django.db.models import Count
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


def search_product(request):
    """Given an user input, the method retrieve a product from the database
    check if it exists, get the category where there is the most occurence and
    display the data in the template.

    Returns:
        [str]: List of the products from the same category
    """
    user_input = request.GET.get("product_search")
    # User input normalization
    user_input = str(user_input).lower().capitalize()
    try:
        # Retrieve product object
        product_name = Product.objects.filter(name=user_input)[0]
        # Retrieve all categories related to a product and take the first one
        category_pk_first = product_name.categories.all()[0].pk
        for cat_number in product_name.categories.all():
            cat = Category.objects.get(pk=cat_number.pk)
            print(cat.categories.all().count())

        # give the cat object the pk of the first category for which product object belong
        cat = Category.objects.get(pk=category_pk_first)
        # order product by nutriscore from the best to worst
        category_products = cat.categories.all().order_by("nutriscore_grade")
        context = {"product": category_products, "origin_product": product_name.pk}
        return render(request, "products/product.html", context)
    except IndexError:
        messages.error(
            request, (f"Impossible de trouver des subsititues à {user_input}")
        )
        return redirect("/")


class ProductDetailView(DetailView):
    """Detail view that lists display information for a given <Model> on a single page
    Args:
        DetailView : Render a "detail" view of an object.
    """

    model = Product


def save_favorite(request):
    """Save a substitue for a product and redirct user to
    the favoris view

    Args:
        id_product (int): Id of the product to be saved
    """
    user = request.user
    product_id = request.POST.get("product_id")
    substitute_id = request.POST.get("substitute_id")

    origin_product = Product.objects.get(pk=product_id)
    product = Product.objects.get(pk=substitute_id)

    Favorite.objects.create(product=origin_product, substitute=product, user=user)
    return redirect("users:fav", user)


def get_all_products(request):
    # TODO: Recherche par prdouit, recupérer le term, term = request.get, pas object all #product object filter

    product = Product.objects.all()
    product = list([product.name for product in product])
    return JsonResponse(product, safe=False)
