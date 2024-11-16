from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

UserModel = get_user_model()

class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)


class AppUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel