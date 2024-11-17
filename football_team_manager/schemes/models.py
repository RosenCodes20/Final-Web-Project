from django.db import models

from football_team_manager.schemes.choices import SchemeChoices


class Scheme(models.Model):

    scheme = models.CharField(
        choices=SchemeChoices.choices
    )