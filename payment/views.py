from django.http import JsonResponse
from django.shortcuts import render
from office import models
from accounts.models import User


def get_request(request):
    return render(request, 'payment/request.html')


def create_req_measure(request):
    if request.method == 'GET':
        return render(request, 'payment/request-measurement.html', context={"services": models.Service.objects.all()})
    elif request.method == 'POST' and request.is_ajax:
        user_id = request.POST.get('user')
        user = User.objects.get(pk=user_id)
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        service = request.POST.get('service')
        serv_obj = models.Service.objects.get(pk=service)
        req_measure = models.RequestMeasurement(address=address, description=desc, user=user, service=serv_obj)
        if req_measure:
            return JsonResponse({"data": 1, "pk": req_measure.pk})
        else:
            return JsonResponse({"data": -1})
    else:
        return render(request, 'payment/request-measurement.html', context={"services": models.Service.objects.all()})


def req_measure_detail(request, pk):
    req = models.RequestMeasurement.objects.get(pk=pk)
    return render(request, 'payment/request_measuremnt_detail.html', context={"req": req})


def req_measure_list(request):
    requests = models.RequestMeasurement.objects.all()
    return render(request, 'payment/request_measuremnt_list.html', context={"requests": requests})


