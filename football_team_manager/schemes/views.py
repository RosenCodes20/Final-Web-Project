from django.shortcuts import render, redirect

from football_team_manager.players.models import Player
from football_team_manager.schemes.forms import CreateSchemeForm
from football_team_manager.schemes.models import Scheme


def scheme_details(request, pk):

    scheme = Scheme.objects.get(id=pk)
    goalkeeper = None

    if request.user.is_authenticated:
        goalkeeper = Player.objects.filter(user=request.user, position="gk").last()
        
    context = {
        "scheme": scheme,
        "goalkeeper": goalkeeper
    }

    return render(request, "scheme/scheme_details.html", context)


def create_scheme(request):

    form = CreateSchemeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            scheme = form.save(commit=False)

            scheme.user = request.user

            scheme.save()

            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "scheme/create_scheme.html", context)