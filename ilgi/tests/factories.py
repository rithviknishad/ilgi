from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

from ..models import Model1

User = get_user_model()


class Model1Factory(DjangoModelFactory):
    class Meta:
        model = Model1

    field1 = factory.Faker("bs")
