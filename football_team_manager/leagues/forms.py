from django import forms
from django.core.exceptions import ValidationError

from football_team_manager.leagues.models import League


class BaseLeagueForm(forms.ModelForm):

    class Meta:
        exclude = ("user", )
        model = League

        labels = {
            "league_name": "League Name:",
            "country": "Country:"
        }

        error_messages = {
            "league_name": {
                "required": "This field is required",
                "invalid": "Enter a valid league name"
            },

            "country": {
                "required": "This field is required",
                "invalid": "Please enter a valid country!!"
            }
        }


    def clean(self):
        country = self.cleaned_data["country"]

        if not country[0].isupper():

            raise ValidationError("Please enter a country that starts with capital letter")


class CreateLeagueForm(BaseLeagueForm):
    pass