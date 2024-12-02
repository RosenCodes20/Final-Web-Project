from rest_framework import serializers

from football_team_manager.players.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        exclude = ('user',)