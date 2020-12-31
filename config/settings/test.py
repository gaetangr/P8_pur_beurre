from .base import *

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="HIBCJYNwbqnBRCJkXFIPwVVLIBsMLVs8MegExOBVfYrL4tI2UlxVhWBryq4xZHLZ",
)
