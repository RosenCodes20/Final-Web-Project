from django import forms

from football_team_manager.schemes.models import Scheme


class SchemeBaseForm(forms.ModelForm):

    class Meta:
        exclude = ("user", )
        model = Scheme


class CreateSchemeForm(SchemeBaseForm):
    pass