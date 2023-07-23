from django.test import TestCase

from .factories import UserFactory


class TestAuth(TestCase):
    def test_login(self):
        """Test that the user can log in."""

        self.user = UserFactory.with_password("secret123")

        resp = self.client.post(
            "/api/v1/auth/login/",
            {"email": self.user.email, "password": "secret123"},
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 200)
        self.assertTrue("key" in resp.json())

    def test_login_failure(self):
        """Test that the login with incorrect password fails."""
        self.user = UserFactory.with_password("secret123")

        resp = self.client.post(
            "/api/v1/auth/login/",
            {"email": self.user.email, "password": "incorrectPassword"},
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 400)

    def test_signup(self):
        """Test that new users can sign up."""

        resp = self.client.post(
            "/api/v1/auth/register/",
            {
                "email": "test@example.com",
                "password1": "S3cr3t?N0tR34lly",
                "password2": "S3cr3t?N0tR34lly",
            },
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 201)
        self.assertTrue("key" in resp.json())
