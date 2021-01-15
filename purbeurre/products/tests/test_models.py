import pytest

from ..models import Product
from .factories import ProductFactory


@pytest.fixture
def product():
    """Create a new product object with abstract datas

    Returns:
        class: Return product factory
    """
    return ProductFactory


pytestmark = pytest.mark.django_db
