from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class BaseTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="12345"
        )
