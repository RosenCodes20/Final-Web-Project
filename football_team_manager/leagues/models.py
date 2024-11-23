from django.contrib.auth import get_user_model
from django.db import models

from football_team_manager.leagues.validators import validate_league_name

UserModel = get_user_model()

class League(models.Model):

    league_name = models.CharField(
        max_length=200,
        validators=[
            validate_league_name
        ]
    )

    country = models.CharField(
        max_length=200,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.league_name
