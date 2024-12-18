from django.contrib.auth import get_user_model
from django.db import models

from football_team_manager.leagues.models import League
from football_team_manager.teams.validators import validate_team_players, validate_team_name

UserModel = get_user_model()

class Team(models.Model):

    team_name = models.CharField(
        max_length=100,
        validators=[
            validate_team_name
        ],
    )

    team_league = models.ForeignKey(
        to=League,
        on_delete=models.CASCADE,
        related_name="leagues",
        blank=True,
        null=True
    )

    players = models.IntegerField(
        validators=[
            validate_team_players
        ]
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.team_name


class MyTeam(models.Model):
    team_name = models.CharField(
        max_length=200
    )

    logo_url = models.URLField()

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )