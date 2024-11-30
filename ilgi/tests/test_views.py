from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from users.tests.factories import UserFactory, AdminUserFactory
from .factories import Model1Factory
from ..serializers import Model1Serializer


class TestModel1(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = Model1Factory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Model1 instances"""

        resp = self.client.get("/api/v1/ilgi/model1/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Model1 collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/ilgi/model1/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Model1 instances"""

        resp = self.client.get(f"/api/v1/ilgi/model1/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Model1 can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/ilgi/model1/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Model1"""

        resp = self.client.post("/api/v1/ilgi/model1/")
        self.assertEqual(resp.status_code, 403)

    @patch("ilgi.views.Model1ViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Model1"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = Model1Serializer(self.instance).data

        resp = self.client.post("/api/v1/ilgi/model1/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Model1"""

        resp = self.client.patch(f"/api/v1/ilgi/model1/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Model1 update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/ilgi/model1/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Model1"""

        resp = self.client.delete(f"/api/v1/ilgi/model1/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Model1 deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/ilgi/model1/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
