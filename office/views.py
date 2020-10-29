from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from accounts.models import User


def show_reply_detail(request, pk):
    context = {
        "reply": models.Reply.objects.get(id=pk)
    }
    return render(request, 'office/reply-detail.html', context)


def reply_list(request, pk):
    customer = User.objects.get(pk=pk)
    context = {"customer_replies": models.Reply.objects.filter(customer=customer)}
    return render(request, 'office/reply-list.html', context)


def send_reply(request):
    if request.method == 'GET':
        return render(request, 'office/reply-form.html')
    elif request.method == 'POST' and request.is_ajax:
        customer_id = request.POST.get('user_id')
        customer = User.objects.get(pk=customer_id)
        content = request.POST.get('content')
        reply = models.Reply(customer=customer, reply_message=content)
        reply.save()
        if reply:
            return JsonResponse({"data": 1, "pk": reply.pk})
        else:
            return JsonResponse({"data": -1})
    else:
        return render(request, 'office/reply-form.html')


def get_customers(request):
    if request.method == 'POST' and request.is_ajax:
        users = User.objects.filter(user_type=3)
        users_json = serializers.serialize('json', users)
        return HttpResponse(users_json, content_type='application/json')


def contact_engineer(request, pk):
    engineer = User.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'office/contact-engineer.html', context={"engineer": engineer})
    elif request.method == 'POST' and request.is_ajax:
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        msg = models.ContactEngineer(engineer_name=engineer, title=title, message=message, sender_name=sender_name,
                                     sender_email=sender_email)
        if msg:
            return JsonResponse({"data": 1, "pk": msg.pk})
        else:
            return JsonResponse({"data": -1})
    else:
        return render(request, 'office/contact-engineer.html', context={"engineer": engineer})


def contact_engineer_detail(request, pk):
    context = {
        "contact": models.ContactEngineer.objects.get(id=pk)
    }
    return render(request, 'office/contact-engineer-detail.html', context)


def contact_engineer_list(request, pk):
    engineer = User.objects.get(pk=pk)
    context = {"engineer_contacts": models.ContactEngineer.objects.filter(engineer_name=engineer)}
    return render(request, 'office/contact-engineer-list.html', context)


def contact_form(request):
    if request.method == 'GET':
        return render(request, 'office/contact-form.html')
    elif request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        cat = request.POST.get('cat')
        city = request.POST.get('city')
        country = request.POST.get('country')
        title = request.POST.get('title')

        contact = models.Contact(email=email, message=message, phone=phone, name=name, category=cat, city=city,
                                 country=country, title=title)
        contact.save()
        if contact.pk:
            return JsonResponse({"data": 1, "pk": contact.pk})
        else:
            return JsonResponse({"data": -1})
    else:
        return render(request, 'office/contact-form.html')


def contact_form_detail(request, pk):
    context = {
        "contact": models.Contact.objects.get(id=pk)
    }
    return render(request, 'office/contact-form-detail.html', context)


def contact_list_detail(request):
    forms = models.Contact.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(forms, 8)
    try:
        forms = paginator.page(page)
    except PageNotAnInteger:
        forms = paginator.page(1)
    except EmptyPage:
        forms = paginator.page(paginator.num_pages)
    context = {
        "forms": forms
    }
    return render(request, 'office/contact-list.html', context=context)


def perform_survey(request):
    services = models.Service.objects.all()
    context = {"Services": services}
    if request.method == 'GET':
        return render(request, 'office/survey.html', context)
    elif request.method == 'POST' and request.is_ajax:
        color = request.POST.get('color')
        interest = request.POST.get('interest')
        quote = request.POST.get('quote')
        service = request.POST.get('service')
        service_obj = models.Service.objects.get(pk=service)
        user_ob = User.objects.get(pk=request.user.pk)
        survey = models.Survey(interests=interest, color=color, service_type=service_obj, quote=quote,
                               user=user_ob)
        if survey:
            return JsonResponse({"data": "1"})
        else:
            return JsonResponse({"data": "-1"})
    else:
        return render(request, 'office/survey.html', context)


def get_Services(request):
    if request.method == 'POST' and request.is_ajax:
        services = models.Service.objects.all()
        services_json = serializers.serialize('json', services)
        return HttpResponse(services_json, content_type='application/json')


def services_type(request):
    context = {"services": models.Service.objects.all()}
    return render(request, 'office/services-type.html', context)


def servey_list(request):
    lists = models.Survey.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lists, 5)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    context = {
        "forms": lists
    }
    return render(request, 'office/survey-list.html', context=context)


def survey_detail(request, pk):
    context = {
        "survey": models.Survey.objects.get(id=pk)
    }
    return render(request, 'office/survey-detail.html', context)


def request_work(request):
    services = models.Service.objects.all()
    user = request.user
    context = {
        "services": services,
        "user": user
    }
    if request.method == 'POST' and request.FILES['picture']:
        selected_service = request.POST.get('selected_service')
        service = models.Service.objects.get(id=selected_service)
        address = request.POST.get('address')
        title = request.POST.get('title')
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(picture.name, picture)
        work = models.RequestWork(customer=user, service=service, address=address, name=title, photo=picture)
        work.save()
        if work is not None:
            return redirect('request_work-detail', work.pk)
    return render(request, 'office/request_work.html', context=context)


def request_work_detail(request, pk):
    request_work_req = models.RequestWork.objects.get(id=pk)
    context = {
        "request_work": request_work_req
    }
    return render(request, 'office/request_work_detail.html', context)


def request_work_list(request):
    context = {"reqs": models.RequestWork.objects.all()}
    return render(request, 'office/req-list.html', context)
