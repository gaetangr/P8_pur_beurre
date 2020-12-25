from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """[summary]

    Args:
        AbstractUser ([type]): [description]
    """
   
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    bio = models.TextField("Bio", blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
