from django.contrib import admin

from football_team_manager.players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_filter = ['name']
    ordering = ['age', 'name']
    list_display = ['name', 'age', 'club']
    search_fields = ['name', 'club__team_name']
    readonly_fields = ['user', 'club']