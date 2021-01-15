from faker import Faker
import factory
import factory.fuzzy

# Models
from mdm_inventory.users.models import Client

#factorie
from mdm_inventory.address.tests.factories import AddressFactory

class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model =  Client
        django_get_or_create = ('dni',)

    first_name = factory.Sequence(lambda n: "client_%s" % n)
    last_name = factory.Sequence(lambda n: "anonimo_%s" % n)
    dni = factory.Sequence(lambda n: "123456789%s" % n)
    phone_number = factory.Sequence(lambda n: '123-555-%04d' % n)
    full_name = factory.LazyAttribute(lambda a: '{}'.format(a.first_name))
    address = factory.SubFactory(AddressFactory)
    def __str__(self):
        return f'{self.first_name } - {self.dni}'