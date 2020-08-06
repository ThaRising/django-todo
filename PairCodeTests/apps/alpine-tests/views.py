from django.shortcuts import render


def index(request):
    return render(
        request,
        "alpine-tests/generic_component.html",
        {}
    )
