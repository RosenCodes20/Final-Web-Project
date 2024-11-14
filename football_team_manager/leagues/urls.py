from django.urls import path

from football_team_manager.leagues import views

urlpatterns = [
    path("create-league/", views.create_league, name="create-league")
]