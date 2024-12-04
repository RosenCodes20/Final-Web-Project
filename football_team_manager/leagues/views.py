from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from football_team_manager.leagues.forms import BaseLeagueForm, CreateLeagueForm


@login_required
def create_league(request):

    if request.method == "GET":
        form = CreateLeagueForm()

    else:
        form = CreateLeagueForm(request.POST)

        if form.is_valid():
            league = form.save(commit=False)

            league.user = request.user

            league.save()

            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "leagues/create-league.html", context)