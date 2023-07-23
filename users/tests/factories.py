import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = factory.Faker("email")
    name = factory.Faker("name")
    is_active = True

    @staticmethod
    def with_password(password, **kwargs):
        user = UserFactory.build(**kwargs)
        user.set_password(password)
        user.save()
        return user


class AdminUserFactory(UserFactory):
    email = factory.Faker("email")
    is_staff = True
    is_superuser = True
    name = factory.Faker("name")
