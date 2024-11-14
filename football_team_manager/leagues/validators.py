from django.core.exceptions import ValidationError


def validate_league_name(value):

    if value.split(" ")[0] == "Efbet":
        raise ValidationError("This is not a valid league!!")