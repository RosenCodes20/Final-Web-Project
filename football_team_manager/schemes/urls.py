from django.urls import path

from football_team_manager.schemes import views

urlpatterns = [
    path("scheme-details/<int:pk>/", views.scheme_details, name="scheme-details"),
    path("create-scheme/", views.create_scheme, name="create-scheme")
]