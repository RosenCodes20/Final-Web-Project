from django import forms

from football_team_manager.leagues.models import League
from football_team_manager.teams.models import Team


class BaseTeamForm(forms.ModelForm):

    class Meta:
        exclude = ("user", )
        model = Team

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields['team_league'].queryset = League.objects.filter(user=user)

class CreateTeamForm(BaseTeamForm):
    pass