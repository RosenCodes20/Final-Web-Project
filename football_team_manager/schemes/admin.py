from django.contrib import admin

from football_team_manager.schemes.models import Scheme


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_filter = ['scheme']
    search_fields = ['scheme']
    readonly_fields = ['user']