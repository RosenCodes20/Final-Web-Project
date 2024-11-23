from django.urls import path

from football_team_manager.common import views

urlpatterns = [
    path("", views.Index.as_view(), name="index")
]