from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Stores a profile, a profile is related to an instance of :model:`auth.User`

    Args:
        AbstractUser : An abstract base class for extending user model
    """

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    bio = models.TextField("Bio", blank=True)

    def get_absolute_url(self):
        """If model is created, return user to specific path"""
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        """Return object with an explicit string name"""
        return self.name
