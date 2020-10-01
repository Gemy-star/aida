from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from accounts.models import User
import smtplib




def show_reply_detail(request, pk):
    context = {
        "reply": models.Reply.objects.get(id=pk)
    }
    return render(request, 'office/reply-detail.html', context)


def reply_form(request, email):
    engineer = User.objects.get(id=request.user.pk)
    user = User.objects.get(email=email)
    context = {
        "engineer": engineer,
        "user": user
    }
    if request.method == 'POST':
        reply = request.POST.get('reply')
        reply_obj = models.Reply(engineer=engineer, customer=user, reply_message=reply)
        reply_obj.save()
        if reply_obj is not None:
            messages.SUCCESS(request, 'Replied Successfully')
            return redirect('reply-detail', pk=reply_obj.pk)
        else:
            messages.error(request, 'Please Review Your Data Failed To Reply')
    return render(request, 'office/reply-form.html', context)


def contact_forms_list(request):
    model = models.Contact.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'office/contact-form-list.html', {"forms": model})


def show_contact_form(request, pk):
    context = {
        "form": models.Contact.objects.get(id=pk)
    }
    return render(request, 'office/contact-form-detail.html', context)


def service_types(request):
    context = {
        "services": models.Service.objects.all()
    }
    return render(request, 'office/services-type.html', context)


def user_detail(request):
    return render(request, 'office/user-detail.html')


def detail_service(request, pk):
    context = {
        "services": models.Service.objects.get(id=pk),
        "designs": models.Service.objects.get(id=pk).designs.all(),
    }
    return render(request, 'office/detail-service.html', context)


def detail_design(request, pk):
    context = {
        "design": models.Design.objects.get(id=pk),
        "engineers": models.Design.objects.get(id=pk).engineer.filter(user_type=2),
    }
    return render(request, 'office/detail-design.html', context)


def detail_engineer(request, pk):
    context = {
        "user": User.objects.get(id=pk),
    }
    return render(request, 'office/engineer-detail.html', context)


def contact_engineer(request, pk):
    engineer = User.objects.get(id=pk)
    if request.method == 'POST':
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        name = request.POST.get('name')
        contact = models.Contact(title=title, sender=email, message=message, engineer=engineer, user_name=name)
        contact.save()
        if contact is not None:
            messages.info(request, 'Thanks For Your Trust')
            return redirect('contact-form-detail', pk=contact.pk)
        else:
            messages.error(request, 'Please Review Your Data Failed To Register')
    context = {'engineer': engineer}
    return render(request, 'office/contact-form.html', context)


def reply_list_customer(request, pk):
    customer = User.objects.get(id=pk)
    model = models.Reply.objects.filter(customer=customer)
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'office/reply-list.html', {"customer_replies": model})


def request_measurement_form(request, pk):
    user = User.objects.get(id=pk)
    context = {
        "services": models.Service.objects.all()
    }
    if request.method == 'POST':
        address = request.POST.get('address')
        message = request.POST.get('desc')
        selected_service = request.POST.get('selected_service')
        service = models.Service.objects.get(id=selected_service)
        measure = models.RequestMeasurement(user=user, description=message, address=address, service=service)
        measure.save()

        if measure is not None:
            messages.SUCCESS(request, 'Check Our Website for answer')
            return redirect('measurement-detail', pk=measure.pk)
        else:
            messages.info(request, 'Error happened')
    return render(request, 'office/request_measurement.html', context)


def request_measurement_detail(request, pk):
    measure = models.RequestMeasurement.objects.get(id=pk)
    context = {
        "measure": measure
    }
    return render(request, 'office/request_measuremnt_detail.html', context)


def request_measurement_list(request):
    model = models.RequestMeasurement.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'office/request_measuremnt_list.html', {"measures": model})


def request_work(request, pk):
    services = models.Service.objects.all()
    user = User.objects.get(id=pk)
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


def survey(request, pk):
    user = User.objects.get(id=pk)
    designs = models.Design.objects.all()
    context = {
        "user": user,
        "designs": designs
    }
    if request.method == 'POST':
        selected_design = request.POST.get('design')
        design = models.Design.objects.get(id=selected_design)
        quote = request.POST.get('quote')
        interest = request.POST.get('interest')
        color = request.POST.get('color')
        survey_obj = models.Survey(user=user, design_type=design, quote=quote, interests=interest, color=color)
        survey_obj.save()
        send_mail('Thanks for Your passion', 'Your answer for our survey has been received',
                  'bauhaus.team.2020@gmail.com',
                  [user.email])
        send_mail('Thanks for Your passion', 'Your answer for our survey has been received',
                  'bauhaus.team.2020@gmail.com',
                  ['m.yassen.93@gmail.com'])
        messages.success(request, 'Thanks for Your Answer')
        if survey_obj is not None:
            return redirect('request-measurement', user.pk)
    return render(request, 'office/Survey.html', context)
