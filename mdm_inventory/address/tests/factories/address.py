from faker import Faker
import factory
import factory.fuzzy

# Models
from mdm_inventory.address.models import Address

#Factories
from mdm_inventory.clients.tests.factories import ClientFactory

class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    country = factory.Sequence(lambda n: "country_%s" % n)
    state = factory.Sequence(lambda n: "state_%s" % n)
    street = factory.Sequence(lambda n: "street_%s" % n)
    municipality = factory.Sequence(lambda n: "municipality_%s" % n)
    is_active = True
    client  = factory.SubFactory(ClientFactory)
    def __str__(self):
        return f'{self.country } - {self.state}'
