import crayons
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from yaspin import yaspin

from purbeurre.users.models import User


class Command(BaseCommand):
    """Creating a superuser for the admin panel with prepopulated datas"""

    help = "Creating a superuser for the admin panel with prepopulated datas"

    def handle(self, *args, **options):
        admin_url = f"http://127.0.0.1:8000/{settings.ADMIN_URL}"
        default_password = "password"
        default_username = "admin"

        print(crayons.yellow("Creating admin user.."))
        try:
            user = User.objects.create_user(
                username=default_username,
                password=default_password,
                first_name="John",
                last_name="Doe",
                is_superuser=True,
                is_staff=True,
                email="admin@admin.com",
            )
            print(crayons.green("✔ Success!"))
            print(
                crayons.normal(
                    f"Username: {crayons.yellow(default_username)} - Password: {crayons.yellow(default_password)} - Connect to: {crayons.yellow(admin_url)}"
                )
            )
        except IntegrityError:
            print(
                crayons.red(
                    "✘ The superuser has already been created! use command: 'python manage.py createsuperuser'"
                )
            )
