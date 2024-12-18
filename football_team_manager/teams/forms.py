from django import forms

from football_team_manager.leagues.models import League
from football_team_manager.teams.models import Team, MyTeam


class BaseTeamForm(forms.ModelForm):

    class Meta:
        exclude = ("user", )
        model = Team

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields['team_league'].queryset = League.objects.filter(user=user)

class BaseMyTeamForm(forms.ModelForm):

    class Meta:
        exclude = ("user", )
        model = MyTeam



class CreateTeamForm(BaseTeamForm):
    pass


class CreateMyTeamForm(BaseMyTeamForm):
    pass