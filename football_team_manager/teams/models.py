from django.db import models

from football_team_manager.leagues.models import League
from football_team_manager.teams.validators import validate_team_players, validate_team_name


class Team(models.Model):

    team_name = models.CharField(
        max_length=100,
        validators=[
            validate_team_name
        ],
        unique=True
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

    def __str__(self):
        return self.team_name
