from django.shortcuts import render, redirect

from football_team_manager.leagues.forms import BaseLeagueForm


def create_league(request):

    if request.method == "GET":
        form = BaseLeagueForm()

    else:
        form = BaseLeagueForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "leagues/create-league.html", context)