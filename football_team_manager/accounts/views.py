from datetime import datetime

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from football_team_manager.accounts.forms import UserRegisterForm, EditProfileForm
from football_team_manager.accounts.models import User, Profile

UserModel = get_user_model()

class Login(UserPassesTestMixin, LoginView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True

    template_name = "logins/login.html"

class Logout(LoginRequiredMixin, LogoutView):
    template_name = "logins/logout.html"
    http_method_names = ['get', 'post']


class Register(UserPassesTestMixin, CreateView):
    template_name = "logins/register.html"
    model = UserModel
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "profile/edit-profile.html"
    form_class = EditProfileForm
    context_object_name = "profile"

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user.profile == user.profile

    def get_success_url(self):

        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.object.user.pk
            }
        )

class ProfileDetails(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = UserModel
    template_name = "profile/profile-details.html"
    context_object_name = "profile"

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user.profile == user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.object

        if model.profile.date_of_birth:
            date_of_birth = model.profile.date_of_birth
            date_of_birth = datetime.combine(date_of_birth, datetime.min.time())

            context["age"] = relativedelta(datetime.now(), date_of_birth).years

        return context


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({
                'access': str(access_token),
                'refresh': str(refresh),
            })

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

