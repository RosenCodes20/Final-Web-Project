from django.template import Library

from football_team_manager.players.models import Player

register = Library()

@register.simple_tag
def get_players():

    return Player.objects.all()