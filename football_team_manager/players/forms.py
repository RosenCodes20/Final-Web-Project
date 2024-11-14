from django import forms

from football_team_manager.players.models import Player


class BasePlayerForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Player

        error_messages = {
            "club": {
                "required": "Please select a club that this player plays in!",
            },

            "name": {
                "unique": "Name should be unique!!!",
                "required": "This field is required!"
            },

            "age": {
                "required": "This field is required",
                "invalid": "Enter a valid age!!"
            }
        }


class PlayerEditForm(BasePlayerForm):
    pass


class PlayerDeleteForm(BasePlayerForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True