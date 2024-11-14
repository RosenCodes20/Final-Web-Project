from django.core.exceptions import ValidationError


def validate_player_age(value):

    if value < 16 or value > 60:
        raise ValidationError("There isn't a player at this age!!")