from django import forms

from football_team_manager.players.models import Player
from football_team_manager.teams.models import Team


class BasePlayerForm(forms.ModelForm):

    class Meta:
        exclude = ("user", )
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

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields['club'].queryset = Team.objects.filter(user=user)

class CreatePlayerForm(BasePlayerForm):
    pass


class PlayerEditForm(BasePlayerForm):
    class Meta(BasePlayerForm.Meta):
        exclude = ("user", "image_photo")


class PlayerDeleteForm(BasePlayerForm):

    class Meta(BasePlayerForm.Meta):
        exclude = ("user", "image_photo")

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True