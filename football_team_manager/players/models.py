from django.contrib.auth import get_user_model
from django.db import models

from football_team_manager.players.choices import PlayerPositionChoices
from football_team_manager.players.validators import validate_player_age
from football_team_manager.teams.models import Team

UserModel = get_user_model()

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

    position = models.CharField(
        choices=PlayerPositionChoices.choices
    )

    image_photo = models.ImageField(
        upload_to="media/"
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )