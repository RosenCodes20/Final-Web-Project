from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from football_team_manager.leagues.models import League
from football_team_manager.teams.forms import BaseTeamForm, CreateTeamForm, CreateMyTeamForm
from football_team_manager.teams.models import Team, MyTeam


@login_required
def create_team(request):

    if not League.objects.filter(user=request.user):
        raise PermissionDenied()

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

@login_required
def create_myteam(request):

    if MyTeam.objects.filter(user=request.user):
        raise PermissionDenied()

    form = CreateMyTeamForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            team = form.save(commit=False)

            team.user = request.user

            team.save()

            return redirect("index")

    context = {
        "form": form,
    }

    return render(request, "teams/create_team_name.html", context)