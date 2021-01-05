from django.conf import settings
from django.core.management.base import BaseCommand

from purbeurre.products.downloader import DataCleaner, Downloader
from purbeurre.products.models import Category, Product
from halo import Halo
import crayons


class Command(BaseCommand):
    """Populate database with OpenFoodfacts Api"""

    help = """Populate database with OpenFoodfacts Api"""

    def handle(self, *args, **options):
        spinner = Halo(
            text="Fetching data and populating database...",
            text_color="yellow",
            spinner="dots",
        )
        downloader = Downloader()
        cleaner = DataCleaner()
        products = downloader.get_product(10, 10)
        categories, products = cleaner.clean(products)
        Category.objects.all().delete()
        for cat in categories:
            Category.objects.create(name=cat)

        Product.objects.all().delete()
        for product in products:
            name = product["product_name"]
            image_url = product["image_url"]  # name
            url = product["url"]  # url product
            categories = product["categories"]  # url product
            nutriscore_grade = product["nutriscore_grade"]  # nutriscore grade
            code = product["code"]
            # code  # img url
            Product.objects.create(
                name=name,
                code=code,
                nutriscore_grade=nutriscore_grade,
                image_url=image_url,
                url=url,
            )
        spinner.succeed(crayons.green("Success!"))
