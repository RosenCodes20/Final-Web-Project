from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from football_team_manager.leagues.models import League

UserModel = get_user_model()

class TestLeagueCreation(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        self.credentials = {
            "league_name": "LaLiga",
            "country": "Spain",
            "user": self.user
        }

    def test_league_creation_successful__returning_to_index(self):
        self.client.login(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        response = self.client.post(reverse('create-league'), data=self.credentials)

        self.assertEqual(League.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(League.objects.filter(user=self.user).first(), League.objects.last())


    def test_league_creation_redirects_us_to_index(self):
        self.client.login(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        response = self.client.post(reverse('create-league'), data=self.credentials)

        self.assertRedirects(response, reverse('index'))