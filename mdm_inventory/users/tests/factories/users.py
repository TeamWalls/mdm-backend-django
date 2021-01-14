from faker import Faker
import factory
import factory.fuzzy

# Models
from mdm_inventory.users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email', 'username',)

    first_name = factory.Sequence(lambda n: "anonimo_%s" % n)
    last_name = factory.Sequence(lambda n: "anonimo_%s" % n)
    username = factory.Sequence(lambda n: "usuario_%s" % n)
    email = factory.LazyAttribute(lambda a: '{}@example.com'.format(a.username).lower(),)
    password = factory.PostGenerationMethodCall('set_password', 'clave123456*')
    is_manager = False
    is_cashier = False
    is_superuser = False
    is_verified = True
    is_staff = False

    def __str__(self):
        return f'{self.email} - {self.username}'