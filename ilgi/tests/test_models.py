from django.test import TestCase

from ..models import Model1
from .factories import Model1Factory


class Model1TestCase(TestCase):
    def test_create_model1(self):
        """Test that Model1 can be created using its factory."""

        obj = Model1Factory()
        assert Model1.objects.all().get() == obj
