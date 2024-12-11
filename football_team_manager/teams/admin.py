from django.contrib import admin

from football_team_manager.teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_filter = ['team_name']
    ordering = ['team_name']
    list_display = ['team_name', 'team_league__league_name']
    search_fields = ['team_name', 'team_league__league_name']
    readonly_fields = ['user', 'team_name']