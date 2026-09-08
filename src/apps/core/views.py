from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    """Muestra las funciones disponibles según el rol del usuario."""

    return render(
        request,
        "core/dashboard.html",
        {"is_administrator": request.user.is_administrator},
    )
