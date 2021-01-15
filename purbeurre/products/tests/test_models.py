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
