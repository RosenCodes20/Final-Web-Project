from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from football_team_manager.leagues.models import League
from football_team_manager.teams.models import Team

UserModel = get_user_model()


class TestTeamCreation(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )


        self.credentials = {
            'team_name': "Barcelona",
            'players': 14,
            'user': self.user
        }


    def test__team_creation_successful__returning_to_index(self):
        self.client.login(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        response = self.client.post(reverse('create-team'), data=self.credentials)

        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_team_creation_successful_redirects_to_index(self):
        self.client.login(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        response = self.client.post(reverse('create-team'), data=self.credentials)

        self.assertRedirects(response, reverse('index'))