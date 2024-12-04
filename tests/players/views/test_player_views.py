from django.contrib.auth import authenticate, login, get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from football_team_manager.accounts.models import User
from football_team_manager.leagues.models import League
from football_team_manager.players.models import Player
from football_team_manager.teams.models import Team

UserModel = get_user_model()
class TestPlayerViews(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email="rosenivanov@gmail.com",
            password="12rosen34"
        )

        league = League.objects.create(
            league_name="Laliga",
            country="Spain",
            user=self.user
        )

        self.team = Team.objects.create(
            team_name="Barcelona",
            players=15,
            team_league=league,
            user=self.user
        )

        self.credentials = {
            "name": "Rosen",
            "age": 20,
            "price": 204124124124,
            "club": self.team,
            "position": "gk",
            "image_photo": "/media/media/ronaldo.png",
            "user": self.user
        }



    def test__player_creation_successful(self):
        self.client.login(
            email="rosenivanov@gmail.com",
            password="12rosen34"
        )

        player = Player.objects.create(**self.credentials)

        player.full_clean()

        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(Player.objects.filter(user=self.user).first(), Player.objects.last())


    def test_create_player_with_invalid_data(self):
        self.client.login(
            email="rosenivanov@gmail.com",
            password="12rosen34"
        )


        with self.assertRaises(ValidationError) as ve:

            self.credentials = {
                "name": 'Rosen',
                "age": 13,
                "price": 204124124124,
                "club": self.team,
                "position": "gk",
                "image_photo": "/media/media/ronaldo.png",
                "user": self.user
            }

            player = Player.objects.create(**self.credentials)
            player.full_clean()
            player.save()

        self.assertEqual(str(ve.exception), '{\'age\': ["There isn\'t a player at this age!!"]}' )