from django.shortcuts import render, redirect

from football_team_manager.players.models import Player
from football_team_manager.schemes.forms import CreateSchemeForm
from football_team_manager.schemes.models import Scheme


def scheme_details(request, pk):

    scheme = Scheme.objects.get(id=pk)

    # goalkeeper = None
    # central1_back352 = None
    # central2_back352 = None
    # central3_back352 = None

    if request.user.is_authenticated:
        goalkeeper = Player.objects.filter(user=request.user, position="gk").last()

        defenders = Player.objects.filter(user=request.user, position="cb")[:3]

        central1_back352 = defenders[0] if len(defenders) > 0 else None
        central2_back352 = defenders[1] if len(defenders) > 1 else None
        central3_back352 = defenders[2] if len(defenders) > 2 else None

        defensive_midfielder352 = Player.objects.filter(user=request.user, position="cdm").last()

        central_midfielders = Player.objects.filter(user=request.user, position="cm")[:2]

        central1_midfielder352 = central_midfielders[0] if len(central_midfielders) > 0 else None
        central2_midfielder352 = central_midfielders[1] if len(central_midfielders) > 1 else None

        left_midfielder352 = Player.objects.filter(user=request.user, position="lm").last()
        right_midfielder352 = Player.objects.filter(user=request.user, position="rm").last()

        strikers = Player.objects.filter(user=request.user, position="st")[:2]

        strikers1_striker352 = strikers[0] if len(strikers) > 0 else None
        strikers2_striker352 = strikers[1] if len(strikers) > 1 else None

    context = {
        "scheme": scheme,
        "goalkeeper352": goalkeeper,
        "central1_back352": central1_back352,
        "central2_back352": central2_back352,
        "central3_back352": central3_back352,
        "defensive_midfielder352": defensive_midfielder352,
        "central1_midfielder352": central1_midfielder352,
        "central2_midfielder352": central2_midfielder352,
        "left_midfielder352": left_midfielder352,
        "right_midfielder352": right_midfielder352,
        "strikers1_striker352": strikers1_striker352,
        "strikers2_striker352": strikers2_striker352,
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