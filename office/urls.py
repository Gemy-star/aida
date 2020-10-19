from django.urls import path
from . import views

urlpatterns = [
    path('services/<int:pk>', views.detail_service, name='detail-service'),
    path('design/<int:pk>', views.detail_design, name='detail-design'),
    path('user/<int:pk>', views.detail_engineer, name='detail-engineer'),
    path('engineer/<int:pk>/contact', views.contact_engineer, name='contact-engineer'),
    path('service/type', views.service_types, name='service-type'),
    path('contact-list', views.contact_forms_list, name='contact-list'),
    path('form/detail/<int:pk>', views.show_contact_form, name='contact-form-detail'),
    path('reply/<str:email>', views.reply_form, name='reply-form'),
    path('reply/detail/<int:pk>', views.show_reply_detail, name='reply-detail'),
    path('reply/list/<int:pk>', views.reply_list_customer, name='reply-list-customer'),
    path('request/<int:pk>', views.request_measurement_form, name='request-measurement'),
    path('request-detail/<int:pk>', views.request_measurement_detail, name='measurement-detail'),
    path('request-list', views.request_measurement_list, name='request-list'),
    path('request-work/<int:pk>', views.request_work, name='request-work'),
    path('request-work/detail/<int:pk>', views.request_work_detail, name='request_work-detail'),
    path('survery/<int:pk>', views.survey, name='survey'),

]
