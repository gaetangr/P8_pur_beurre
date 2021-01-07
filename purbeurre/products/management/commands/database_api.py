# flake8: noqa
import crayons
from django.conf import settings
from django.core.management.base import BaseCommand
from halo import Halo

from purbeurre.products.downloader import DataCleaner, Downloader
from purbeurre.products.models import Category, Product


class Command(BaseCommand):
    """Populate database with OpenFoodfacts Api"""

    help = """Populate database with OpenFoodfacts Api"""

    def handle(self, *args, **options):
        spinner = Halo(
            text="Fetching data and populating database...",
            text_color="yellow",
            spinner="dots",
        )
        spinner.start()

        for category in Category.objects.all():
            # efface les relations entre product et table d'asso...
            category.product_set.clear()
        Category.objects.all().delete()
        Product.objects.all().delete()

        downloader = Downloader()
        cleaner = DataCleaner()
        products = downloader.get_product(10, 10)
        categories, products = cleaner.clean(products)

        for cat in categories:
            Category.objects.create(name=cat)
        for product in products:
            name = product["product_name"]  # name
            image_url = product["image_url"]  # img url
            url = product["url"]  # url product
            nutriscore_grade = product["nutriscore_grade"]  # nutriscore grade
            code = product["code"]

            product_instance = Product.objects.create(
                name=name,
                code=code,
                nutriscore_grade=nutriscore_grade,
                image_url=image_url,
                url=url,
            )
            print(len(product["categories"]))
            print(len(categories))
            for category in product["categories"]:
                category = Category.objects.get(name=category)
                product_instance.categories.add(category)

        spinner.succeed(crayons.green("Success!"))
