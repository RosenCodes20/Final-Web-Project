from django.db import models

from football_team_manager.players.validators import validate_player_age
from football_team_manager.teams.models import Team


class Player(models.Model):

    name = models.CharField(
        max_length=100
    )

    age = models.IntegerField(
        validators=[
            validate_player_age
        ]
    )

    price = models.BigIntegerField()

    club = models.ForeignKey(
        to=Team,
        on_delete=models.CASCADE,
        related_name="teams"
    )

    image_url = models.URLField()
