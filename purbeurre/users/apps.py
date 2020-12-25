from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "purbeurre.users"
    # for translation
    verbose_name = _("Users")
