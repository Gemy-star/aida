from django.shortcuts import render
from office.models import Service


def home(request):
    services = Service.objects.all()
    context = {"services": services}
    return render(request, 'main/home.html', context=context)


def about(request):
    return render(request, 'main/about.html')