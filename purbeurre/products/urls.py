from django.urls import path

from . import views


app_name = "products"
urlpatterns = [
    path(route="", view=views.ProductListView.as_view(), name="list"),
    path("all/", views.get_all_products),
    path("save/", views.save_favorite),
    path(route="<int:pk>", view=views.ProductDetailView.as_view(), name="detail"),
]
