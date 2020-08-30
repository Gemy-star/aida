from django.shortcuts import render
from office import models


def service_cycle(request):
    context = {
        "services": models.Service.objects.all()
    }
    return render(request, 'payment/start_cycle.html', context)


def design_cycle(request):
    context = {
        "designs": models.Design.objects.all()
    }
    return render(request, 'payment/design_cycle.html', context)


def engineer_cycle(request):
    context = {
        "engineers": models.User.objects.filter(user_type=2)
    }
    return render(request, 'payment/engineer_cycle.html', context)


def final_tour(request):
    return render(request, 'payment/final_tour.html')
