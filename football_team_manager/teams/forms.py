from django import forms

from football_team_manager.teams.models import Team


class BaseTeamForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Team