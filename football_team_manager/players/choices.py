from django.db import models


class PlayerPositionChoices(models.TextChoices):

    GOALKEEPER = "gk", "Goalkeeper"
    RIGHT_BACK = "rb", "Right Back"
    LEFT_BACK = "lb", "Left Back"
    CENTRAL_BACK = "cb", "Central Back"
    DEFENSIVE_MIDFIELDER = "cdm", "Defensive Midfielder"
    CENTRAL_MIDFIELDER = "cm", "Central Midfielder"
    LEFT_MIDFIELDER = "lm", "Left Midfielder"
    RIGHT_MIDFIELDER = "rm", "Right Midfielder"
    LEFT_WINGER = "lw", "Left Winger"
    RIGHT_WINGER = "rw", "Right Winger"
    STRIKER = "st", "Striker"