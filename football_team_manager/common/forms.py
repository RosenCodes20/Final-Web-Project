from django import forms
from django.forms import TextInput


class SearchForm(forms.Form):

    player = forms.CharField(
        max_length=300,
        required=False,
        widget=TextInput(attrs={
            "placeholder": "Search for a player......"
        },
        ),
        label=""
    )