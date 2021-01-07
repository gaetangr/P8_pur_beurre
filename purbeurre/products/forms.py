from django import forms
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator

from purbeurre.products.models import Product


class ProductSearchForm(forms.ModelForm):
    """Form for searching a product to substituted."""

    name = forms.CharField(
        min_length=2,
        max_length=100,
        required=True,
        validators=[MinLengthValidator, MaxLengthValidator],
        widget=forms.TextInput(attrs={"placeholder": "Chercher un aliment"}),
    )

    class Meta:
        model = Product
        fields = ["name"]
