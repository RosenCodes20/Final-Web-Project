from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from football_team_manager.players.forms import PlayerEditForm, PlayerDeleteForm, BasePlayerForm, CreatePlayerForm
from football_team_manager.players.models import Player
from football_team_manager.players.serializers import PlayerSerializer


def create_player(request):

    form = CreatePlayerForm(request.POST or None, request.FILES or None, user=request.user)

    if request.method == "POST":

        if form.is_valid():
            player = form.save(commit=False)

            player.user = request.user

            player.save()

            return redirect("index")


    context = {
        "form": form
    }

    return render(request, "players/create-player.html", context)


def delete_player(request, pk):

    player = Player.objects.get(id=pk)

    if request.method == "GET":
        form = PlayerDeleteForm(instance=player, user=request.user)

    else:
        form = PlayerDeleteForm(request.POST, instance=player)

        player.delete()

        return redirect("index")


    context = {
        "player": player,
        "form": form
    }

    return render(request, "players/delete-player.html", context)


def edit_player(request, pk):

    player = Player.objects.get(id=pk)

    if request.method == "GET":
        form = PlayerEditForm(instance=player, user=request.user)

    else:
        form = PlayerEditForm(request.POST, instance=player)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "player": player,
        "form": form
    }

    return render(request, "players/edit-player.html", context)


def player_details(request, pk):

    player = Player.objects.get(id=pk)

    context = {
        "player": player
    }

    return render(request, "players/player_details.html", context)


class ListPlayersView(APIView):
    def get(self, request, *args, **kwargs):
        players = Player.objects.filter(user=request.user)
        serializer = PlayerSerializer(players, many=True)
        return Response({"players": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    