from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls.conf import include

from football_team_manager.accounts import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),

    path("profile/", include([
        path("edit-profile", views.edit_profile, name="edit-profile"),
        path("profile-details", views.profile_details, name="profile-details")
    ])),
]
