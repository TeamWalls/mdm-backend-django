from faker import Faker
import factory
import factory.fuzzy

# Models
from mdm_inventory.products.models import Product


BRAND = [
    ('marca1', 'Marca1'),
    ('marca2', 'Marca2'),
    ('marca3', 'Marca3')
]

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model =  Product
        django_get_or_create = ('code',)

    name = factory.Sequence(lambda n: "product_%s" % n)
    description  = factory.Sequence(lambda n: "description_of_product_%s" % n)
    code = factory.Sequence(lambda n: "#000_%s" % n)
    brand = factory.Faker(
        'random_element', elements=[x[0] for x in BRAND]
    )
    product_type = factory.Sequence(lambda n: "type_%s" % n)
    gross_price = factory.Sequence(lambda n: '1%04d' % n)
    price_neto = factory.Sequence(lambda n: '2%04d' % n)

    def __str__(self):
        return f'{self.name } - {self.code}'