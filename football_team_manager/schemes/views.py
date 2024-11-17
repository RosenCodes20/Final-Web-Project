from django.shortcuts import render, redirect

from football_team_manager.schemes.forms import CreateSchemeForm


def scheme_details(request):

    return render(request, "scheme/scheme_details.html")


def create_scheme(request):

    form = CreateSchemeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "scheme/create_scheme.html", context)