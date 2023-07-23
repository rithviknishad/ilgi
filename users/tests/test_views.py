from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from ..serializers import UserSerializer
from .factories import AdminUserFactory, UserFactory


class TestUser(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()

    def test_non_admin_list_fails(self):
        """Test that regular users can't list other users"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/users/user/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that admins can list users"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.get("/api/v1/users/user/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 2)

        user_ids = {user["id"] for user in data["results"]}
        self.assertEqual(user_ids, {self.user.id, self.admin.id})

    def test_non_admin_get_fails(self):
        """Test that regular users can't retrieve other user's data"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/users/user/{self.admin.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get_self(self):
        """Test that users can their own user data"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/users/user/{self.user.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.user.id)

    def test_get_other(self):
        """Test that admins can get other user's data"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.get(f"/api/v1/users/user/{self.user.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.user.id)

    def test_non_admin_create_fails(self):
        """Test that regular users can't create a new user"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.post("/api/v1/users/user/")
        self.assertEqual(resp.status_code, 403)

    @patch("users.views.UserViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for users.User"""

        self.client.force_authenticate(user=self.admin)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = UserSerializer(self.user).data

        resp = self.client.post("/api/v1/users/user/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_non_admin_update_fails(self):
        """Test that anonymous users can't update user data"""

        resp = self.client.patch(f"/api/v1/users/user/{self.user.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test admins can update user data"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/users/user/{self.user.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_non_admin_delete_fails(self):
        """Test that regular users can't delete users"""

        resp = self.client.delete(f"/api/v1/users/user/{self.user.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test admins can delete users"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/users/user/{self.user.id}/")
        self.assertEqual(resp.status_code, 204)
