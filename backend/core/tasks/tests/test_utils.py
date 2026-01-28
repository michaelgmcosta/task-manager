from .test_base import BaseTest


class AuthenticatedAPITest(BaseTest):

    def setUp(self):
        super().setUp()

        response = self.client.post("/api/auth/login/", {
            "username": "test",
            "password": "12345"
        })

        self.access_token = response.data["access"]
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )