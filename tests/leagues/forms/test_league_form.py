from django.contrib.auth import get_user_model
from django.test import TestCase

from football_team_manager.leagues.forms import BaseLeagueForm

UserModel = get_user_model()
class TestLeagueBaseForm(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email="rosenivanov@gmail.com",
            password="12rosen34"
        )

        self.credentials = {
            "league_name": "premier league",
            "country": "Spain",
            "user": self.user
        }

    def test__league_base_form__expect__true(self):
        form = BaseLeagueForm(data=self.credentials)

        self.assertTrue(form.is_valid())


    def test__league_name__not_entered(self):
        self.credentials['league_name'] = ''

        form = BaseLeagueForm(data=self.credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('league_name', form.errors)

    def test__country__entered_with_small_letters(self):
        self.credentials['country'] = 'spain'
        form = BaseLeagueForm(data=self.credentials)

        self.assertFalse(form.is_valid())

    def test_team_league_name_too_long(self):
        self.credentials['league_name'] = 'r' * 201

        form = BaseLeagueForm(data=self.credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('league_name', form.errors)


