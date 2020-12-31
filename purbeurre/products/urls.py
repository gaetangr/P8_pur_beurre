from django.urls import path

from purbeurre.products.views import get_all_products

app_name = "products"
urlpatterns = [
    path("all/", view=get_all_products),
]
