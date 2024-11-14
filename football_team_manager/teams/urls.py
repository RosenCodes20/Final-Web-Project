from django.urls import path

from football_team_manager.teams import views

urlpatterns = [
    path("create-team/", views.create_team, name="create-team")
]