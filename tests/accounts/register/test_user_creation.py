from django.contrib.auth import get_user_model
from django.test import TestCase

from football_team_manager.accounts.models import User

UserModel = get_user_model()
class TestUserCreation(TestCase):


    def test__valid__user__creation(self):
        user = UserModel.objects.create_user(
            email="rosenivanov@gmail.com",
            password="12admin34"
        )

        user.full_clean()

        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(user, UserModel.objects.get(email="rosenivanov@gmail.com"))