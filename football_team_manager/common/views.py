from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from football_team_manager.common.forms import SearchForm
from football_team_manager.players.models import Player
from football_team_manager.schemes.models import Scheme


class Index(ListView):
    template_name = "common/index.html"
    model = Player
    paginate_by = 2
    context_object_name = "filtered_players"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["player_search_form"] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):

        queryset = self.model.objects.all()

        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        else:
            queryset = []

        if self.request.user.is_authenticated:
            if "player" in self.request.GET:
                player = self.request.GET.get("player")
                queryset = queryset.filter(name__icontains=player)

        return queryset