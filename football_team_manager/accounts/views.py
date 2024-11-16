from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from football_team_manager.accounts.forms import UserRegisterForm

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


def edit_profile(request):

    return render(request, "profile/edit-profile.html")


def profile_details(request):

    return render(request, "profile/profile-details.html")