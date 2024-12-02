from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls.conf import include

from football_team_manager.accounts import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("api/login/", views.LoginView.as_view(), name="api_login"),

    path("profile/<int:pk>/", include([
        path("edit/", views.EditProfile.as_view(), name="edit-profile"),
        path("details/", views.ProfileDetails.as_view(), name="profile-details")
    ])),
]
