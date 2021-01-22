from django.urls import path

from purbeurre.users.views import (
    fav_detail_view,
    user_create_view,
    user_detail_view,
    user_login_view,
    user_logout_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("fav/<str:pk>/", view=fav_detail_view, name="fav"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path(route="create/", view=user_create_view, name="create"),
    path("~update/", view=user_update_view, name="update"),
    path("login/", view=user_login_view, name="login"),
    path("logout/", view=user_logout_view, name="logout"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
    path("fav/<int:pk>/", view=fav_detail_view, name="fav"),
]
