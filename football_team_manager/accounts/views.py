import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from football_team_manager.accounts.forms import UserRegisterForm, EditProfileForm
from football_team_manager.accounts.models import User, Profile

UserModel = get_user_model()

class Login(LoginView):
    template_name = "logins/login.html"

class Logout(LogoutView):
    template_name = "logins/logout.html"
    http_method_names = ['get', 'post']

class Register(CreateView):
    template_name = "logins/register.html"
    model = UserModel
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")


class EditProfile(UpdateView):
    model = Profile
    template_name = "profile/edit-profile.html"
    form_class = EditProfileForm
    context_object_name = "user"

    def get_success_url(self):

        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.object.user.pk
            }
        )

class ProfileDetails(DetailView):
    model = UserModel
    template_name = "profile/profile-details.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.object

        if model.profile.date_of_birth:
            context["age"] = datetime.date.today().year - model.profile.date_of_birth.year

        return context