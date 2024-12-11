from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from football_team_manager.accounts.models import User

UserModel = get_user_model()
class TestUserCreation(TestCase):


    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        self.credentials = {
            'email': 'rosenivanov@gmail.com',
            'password': '12admin34'
        }

    def test__valid__user__login(self):

        response = self.client.post(reverse('login'), data=self.credentials)

        self.assertTrue(self.user.is_authenticated)
        self.assertFalse(self.user.is_anonymous)
