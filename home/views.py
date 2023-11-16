from django.shortcuts import render

from home.models import UzAuto


def example(request):
    auto = UzAuto.objects.all()
    contex = {
        'auto':auto
    }
    return render(request, 'index.html',)

