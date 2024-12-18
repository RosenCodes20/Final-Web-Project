from django.urls import path

from football_team_manager.teams import views

urlpatterns = [
    path("create-team/", views.create_team, name="create-team"),
    path("create-myteam/", views.create_myteam, name='create-team-name')
]