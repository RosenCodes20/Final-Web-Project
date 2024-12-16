import datetime as dt

from datetime import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import DateInput, TextInput

from football_team_manager.accounts.models import Profile

UserModel = get_user_model()

class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)


class AppUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user", )

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data["date_of_birth"]

        date_of_birth = datetime.combine(date_of_birth, datetime.min.time())

        if date_of_birth > datetime.now():

            raise ValidationError("You cannot enter a date in future!")

        return date_of_birth

class EditProfileForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):

        widgets = {
            "date_of_birth": TextInput(attrs={"type": "date"})
        }
