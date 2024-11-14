from django.shortcuts import render, redirect

from football_team_manager.teams.forms import BaseTeamForm


def create_team(request):

    if request.method == "GET":
        form = BaseTeamForm()

    else:
        form = BaseTeamForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")


    context = {
        "form": form
    }

    return render(request, "teams/create_team.html", context)