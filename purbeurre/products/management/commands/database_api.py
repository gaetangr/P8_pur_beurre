from django.conf import settings
from django.core.management.base import BaseCommand

from purbeurre.products.downloader import DataCleaner, Downloader
from purbeurre.products.models import Category, Product

downloader = Downloader()
cleaner = DataCleaner()

products = downloader.get_product(100, 10)
categories, products = cleaner.clean(products)


class Command(BaseCommand):
    """Populate database with OpenFoodfacts Api"""

    help = """Populate database with OpenFoodfacts Api"""

    def handle(self, *args, **options):
        Category.objects.all().delete()
        for cat in categories:
            Category.objects.create(name=cat)

        Product.objects.all().delete()
        for product in products:
            Category.objects.all()
            name = product["product_name"]  # name
            url = product["url"]  # url product
            nutriscore_grade = product["nutriscore_grade"]  # nutriscore grade
            code = product["code"]
            # code  # img url
            Product.objects.create(
                name=name,
                code=code,
                nutriscore_grade=nutriscore_grade,
                url=url,
                categories=cate,
            )
