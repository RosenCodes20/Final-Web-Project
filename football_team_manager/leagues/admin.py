from django.contrib import admin

from football_team_manager.leagues.models import League


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_filter = ['league_name']
    ordering = ['country', 'league_name']
    list_display = ['league_name', 'country']
    search_fields = ['league_name']
    readonly_fields = ['user']