# flake8: noqa
""" Unit tests related to users/views"""
import pytest
from django.urls import reverse

from .factories import ProductFactory

from purbeurre.users.tests.factories import UserFactory


@pytest.fixture
def user():
    """Create a new user object with abstract datas

    Returns:
        class: Return user factory
    """
    return UserFactory


@pytest.fixture
def product():
    """Create a new product object with abstract datas

    Returns:
        class: Return product factory
    """
    return ProductFactory


@pytest.mark.django_db
def test_if_detail_view_can_be_access_by_user(client, user, product):
    """Test if a product detail view can be access by a user """
    user = user
    product = product
    url = reverse("products:detail", kwargs={"pk": product.pk})
    assert url == reverse("products:detail", kwargs={"pk": product.pk})
