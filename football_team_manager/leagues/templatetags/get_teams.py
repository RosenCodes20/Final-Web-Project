from django.template import Library

from football_team_manager.teams.models import Team

register = Library()


@register.simple_tag
def get_teams():
    return Team.objects.all()