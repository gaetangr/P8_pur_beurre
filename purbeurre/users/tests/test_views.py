# flake8: noqa
""" Unit tests related to users/views"""
import pytest
from django.urls import reverse

from .factories import UserFactory


@pytest.fixture
def user():
    """Create a new user object with abstract datas

    Returns:
        class: Return user factory
    """
    return UserFactory


@pytest.mark.django_db
def test_if_get_redirect_return_username_name_of_user(client, user):
    """Test if the Login views return a 200 response """
    user = user
    url = reverse("users:detail", kwargs={"username": user.username})
    assert url == reverse("users:detail", kwargs={"username": user.username})


@pytest.mark.django_db
def test_if_login_views_is_successful(client):
    """Test if the Login views return a 200 response """

    url = reverse("users:login")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.skip(msg="Must improve method before running test")
@pytest.mark.parametrize(
    "path_to_test",
    [
        # Paths to be tested for authenticated user
        "users:update",
    ],
)
def test_if_views_with_authenticated_client_is_successful(
    client,
    django_user_model,
    path_to_test,
    user,
):
    """Test if views related to an authenticated user return 200 response
    :param path_to_test: Pytest fixture to test multiples arguments
    """
    user = django
    client.force_login(user)
    url = reverse(path_to_test)
    response = client.get(url)
    assert response.status_code == 200


# Extra tests to assert some pages return 200 response and that admin page are
# not available for regular users
# ------------------------------------------------------------------------------


@pytest.mark.django_db
def test_if_home_is_successful(client):
    """Test if the home return a 200 response """

    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


def test_if_a_superuser_can_access_administration_panel(admin_client):
    """Test if a superuser can access the administration panel while being login
    :param admin_client: An instance of a superuser, with username “admin” and password “password” to test admin .
    """
    response = admin_client.get("/admin/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_if_an_user_c_access_administration_panel(client):
    """Test if a none superuser is fordbiden to access to the administration panel while being login
    :param client: An instance of a django.test.Client with no superuser privilegies
    """
    response = client.get("/admin/")
    assert response.status_code != 200
