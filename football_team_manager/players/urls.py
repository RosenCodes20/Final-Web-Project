
from django.urls import path

from football_team_manager.players import views

urlpatterns = [
    path("create-player/", views.create_player, name="create-player"),
    path("delete-player/<int:pk>/", views.delete_player, name="delete-player"),
    path("edit-player/<int:pk>/", views.edit_player, name="edit-player"),
    path("player-details/<int:pk>/", views.player_details, name="player-details"),
    path("api/players/", views.ListPlayersView.as_view(), name="api-players"),
]