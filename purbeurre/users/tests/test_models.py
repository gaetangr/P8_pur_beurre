import pytest

from purbeurre.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url():
    user = User.objects.create_user(username="Gaetan")
    assert user.get_absolute_url() == f"/users/{user.username}/"
