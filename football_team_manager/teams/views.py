from django.shortcuts import render, redirect

from football_team_manager.leagues.models import League
from football_team_manager.teams.forms import BaseTeamForm, CreateTeamForm
from football_team_manager.teams.models import Team


def create_team(request):


    if request.method == "GET":
        form = CreateTeamForm(user=request.user)

    else:
        form = CreateTeamForm(request.POST)

        if form.is_valid():
            team = form.save(commit=False)

            team.user = request.user

            team.save()

            return redirect("index")


    context = {
        "form": form
    }

    return render(request, "teams/create_team.html", context)