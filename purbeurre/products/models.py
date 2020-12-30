from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

# models needed => Link image, img-nutrition-url -or- data,


class Category(models.Model):
    """ Models for a category, related to a product"""

    name = models.CharField(
        _("Name"),
        unique=True,
        max_length=100,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        """Return object with an explicit string name"""
        return self.name


class Product(models.Model):
    """ Models related to product """

    # Required fields
    code = models.CharField("Code", max_length=13, unique=True)

    name = models.CharField(_("Name"), max_length=100)

    nutriscore_grade = models.CharField(_("Nutriscode Grade"), max_length=1)

    url = models.URLField(help_text=_("Url to the openfoodfacts website"))

    image_url = models.URLField(blank=True)

    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        """Return object with an explicit string name"""
        return self.name
