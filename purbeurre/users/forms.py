from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _

from .models import User


class CreationUserForm(forms.ModelForm):

    username = forms.CharField(
        label=_("Username"),
        help_text=_("Will be shown to your profile, username is shown publicly"),
        widget=TextInput(attrs={"autofocus": "", "placeholder": "Ex : CheeseLover"}),
    )

    email = forms.CharField(
        label="Email",
        help_text=_("Will be used to send a new password and login on the plateform"),
        widget=TextInput(
            attrs={"autofocus": "", "placeholder": "Ex : ratatouille@goodcheese.com"},
        ),
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={"autofocus": ""}),
        help_text=_("Choose a strong password"),
    )

    confirm_password = forms.CharField(
        label=_("Password confirmation"),
        widget=PasswordInput(attrs={"autofocus": ""}),
        help_text=_("Just to be sure.. confirm your password !"),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                _("Password and password confirmation does not match"),
            )
