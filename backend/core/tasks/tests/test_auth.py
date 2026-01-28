from rest_framework import status
from .test_base import BaseTest


class TaskAuthTest(BaseTest):

    def setUp(self):
        super().setUp()

    def test_login_returns_jwt_token(self):
        """
        Garante que o login retorna access e refresh tokens.
        """
        response = self.client.post("/api/auth/login/", {
            "username": "test",
            "password": "12345"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_access_protected_route_without_token(self):
        """
        Garante que rotas protegidas bloqueiem acesso sem token.
        """
        response = self.client.get("/api/tasks/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_protected_route_with_token(self):
        """
        Garante acesso autorizado com JWT válido.
        """
        login = self.client.post("/api/auth/login/", {
            "username": "test",
            "password": "12345"
        })

        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)