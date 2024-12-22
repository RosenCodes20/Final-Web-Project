from django.urls import path

from football_team_manager.schedules import views

urlpatterns = [
    path('schedule-details/<int:pk>/', views.schedule_details, name='schedule-details'),
    path('add-event/', views.add_event, name='add-event'),
    path('all-events/<int:pk>/', views.all_events, name='all-events'),
    path('game-events/<int:pk>/', views.game_events, name='game-events'),
    path('training-events/<int:pk>/', views.training_events, name='training-events')
]