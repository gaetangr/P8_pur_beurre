import pytest

from .factories import ProductFactory
from ..models import Product


@pytest.fixture
def product():
    """Create a new product object with abstract datas

    Returns:
        class: Return product factory
    """
    return ProductFactory


pytestmark = pytest.mark.django_db


def test__str__(product):
    """If an user object is created, it should return the object with username"""
    product = product
    assert product.__str__() == product.name
    assert str(product) == product.name
