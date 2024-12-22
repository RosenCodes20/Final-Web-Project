from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from football_team_manager.schedules.models import Event


class EventBaseForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ("user", )

        widgets = {
            "date": forms.TextInput(attrs={"type": "date"}),
            "time": forms.TextInput(attrs={"type": "time"}),
            "location": forms.TextInput(attrs={"type": "location"}),
            "is_training": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }


    def clean_date(self):
        date = self.cleaned_data["date"]

        date = datetime.combine(date, datetime.min.time())

        if date < datetime.now():
            raise ValidationError("You cannot enter a date that is passed!")

        return date

class CreateEventForm(EventBaseForm):
    pass