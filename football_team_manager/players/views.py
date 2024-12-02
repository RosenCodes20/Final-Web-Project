from django.shortcuts import render, redirect
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

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


class ListPlayersView(ListAPIView):
    model = Player
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()

        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        return queryset

@extend_schema(
    request=PlayerSerializer,
    responses={201: PlayerSerializer, 400: PlayerSerializer},
)
class PlayerCreateView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    model = Player
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        user = self.request.user
        player = serializer.save(user=user)
        return player


class PlayerDetailsView(RetrieveAPIView):
    serializer_class = PlayerSerializer
    model = Player

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        return queryset


class DeletePlayerView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        player = Player.objects.get(id=pk)

        player.delete()

        return Response(data={"message": "Successfully deleted player!"}, status=status.HTTP_204_NO_CONTENT)


class EditPlayerView(UpdateAPIView):
    model = Player
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        return queryset
