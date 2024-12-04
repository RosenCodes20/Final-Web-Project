
from django.urls import path, include

from football_team_manager.players import views

urlpatterns = [
    path("create-player/", views.CreatePlayerView.as_view(), name="create-player"),
    path("delete-player/<int:pk>/", views.DeletePlayer.as_view(), name="delete-player"),
    path("edit-player/<int:pk>/", views.EditPlayer.as_view(), name="edit-player"),
    path("player-details/<int:pk>/", views.PlayerDetails.as_view(), name="player-details"),
    path("api/players/", views.ListPlayersView.as_view(), name="api-players"),
    path("api/create-player/", views.PlayerCreateView.as_view(), name="api-create-player"),
    path("api/player/<int:pk>/", views.PlayerDetailsView.as_view(), name="api-player-details"),
    path("api/delete-player/<int:pk>/", views.DeletePlayerView.as_view(), name="api-delete-player"),
    path("api/edit-player/<int:pk>/", views.EditPlayerView.as_view(), name="api-edit-player"),
]
