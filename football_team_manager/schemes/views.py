from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from football_team_manager.players.models import Player
from football_team_manager.schemes.forms import CreateSchemeForm
from football_team_manager.schemes.models import Scheme


def test_func(request, pk):
    scheme = get_object_or_404(Player, pk=pk)
    return request.user == scheme.user

@login_required
def scheme_details(request, pk):

    scheme = Scheme.objects.get(id=pk)

    if scheme.user != request.user:
        raise PermissionDenied()

    #
    # goalkeeper = None
    # central1_back352 = None
    # central2_back352 = None
    # central3_back352 = None
    # left_back352 = None
    # right_back352 = None
    # defensive_midfielder352 = None
    # central1_midfielder352 = None
    # central2_midfielder352 = None
    # central3_midfielder352 = None
    # left_midfielder352 = None
    # right_midfielder352 = None
    # left_winger352 = None
    # right_winger352 = None
    # strikers1_striker352 = None
    # strikers2_striker352 = None


    if request.user.is_authenticated:
        goalkeeper = Player.objects.filter(user=request.user, position="gk").last()

        defenders = Player.objects.filter(user=request.user, position="cb")[:3]

        central1_back352 = defenders[0] if len(defenders) > 0 else None
        central2_back352 = defenders[1] if len(defenders) > 1 else None
        central3_back352 = defenders[2] if len(defenders) > 2 else None

        defensive_midfielder352 = Player.objects.filter(user=request.user, position="cdm").last()

        central_midfielders = Player.objects.filter(user=request.user, position="cm")[:3]

        central1_midfielder352 = central_midfielders[0] if len(central_midfielders) > 0 else None
        central2_midfielder352 = central_midfielders[1] if len(central_midfielders) > 1 else None
        central3_midfielder352 = central_midfielders[2] if len(central_midfielders) > 2 else None

        left_midfielder352 = Player.objects.filter(user=request.user, position="lm").last()
        right_midfielder352 = Player.objects.filter(user=request.user, position="rm").last()

        strikers = Player.objects.filter(user=request.user, position="st")[:2]

        strikers1_striker352 = strikers[0] if len(strikers) > 0 else None
        strikers2_striker352 = strikers[1] if len(strikers) > 1 else None

        left_back352 = Player.objects.filter(user=request.user, position="lb").last()
        right_back352 = Player.objects.filter(user=request.user, position="rb").last()

        left_winger352 =  Player.objects.filter(user=request.user, position="lw").last()
        right_winger352 = Player.objects.filter(user=request.user, position="rw").last()

    context = {
        "scheme": scheme,
        "goalkeeper352": goalkeeper,
        "central1_back352": central1_back352,
        "central2_back352": central2_back352,
        "central3_back352": central3_back352,
        "left_back352": left_back352,
        "right_back352": right_back352,
        "defensive_midfielder352": defensive_midfielder352,
        "central1_midfielder352": central1_midfielder352,
        "central2_midfielder352": central2_midfielder352,
        "central3_midfielder352": central3_midfielder352,
        "left_midfielder352": left_midfielder352,
        "right_midfielder352": right_midfielder352,
        "left_winger352": left_winger352,
        "right_winger352": right_winger352,
        "strikers1_striker352": strikers1_striker352,
        "strikers2_striker352": strikers2_striker352,
    }

    return render(request, "scheme/scheme_details.html", context)

@login_required
def create_scheme(request):

    if Scheme.objects.filter(user=request.user):
        raise PermissionDenied()

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