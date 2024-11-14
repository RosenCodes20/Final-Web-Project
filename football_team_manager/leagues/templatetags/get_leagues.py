from django.template import Library

from football_team_manager.leagues.models import League

register = Library()


@register.simple_tag
def get_leagues():
    return League.objects.all()