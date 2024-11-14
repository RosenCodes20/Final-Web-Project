from django.core.exceptions import ValidationError


def validate_team_name(value):

    if "Slavia" in value:
        raise ValidationError("This is not a good team!!!")


def validate_team_players(value):

    if value < 11:
        raise ValidationError("Team should be at least 11 players!!")