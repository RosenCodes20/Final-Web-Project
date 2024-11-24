from django.contrib.auth import get_user_model
from django.db import models

from football_team_manager.schemes.choices import SchemeChoices

UserModel = get_user_model()

class Scheme(models.Model):

    scheme = models.CharField(
        choices=SchemeChoices.choices
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )