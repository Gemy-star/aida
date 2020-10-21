from django.urls import path
from . import views

urlpatterns = [
    path('reply/detail/<int:pk>', views.show_reply_detail, name='reply-detail'),
    path('reply/list/<int:pk>', views.reply_list, name='reply-list'),
    path('send/reply', views.send_reply, name='send-reply'),
    path('get/customers', views.get_customers, name='get-customers'),
    path('contact/engineer/<int:pk>', views.contact_engineer, name='contact-engineer'),
    path('contact/detail/<int:pk>', views.contact_engineer_detail, name='contact-engineer-detail'),
    path('contact/engineer/<int:pk>/list', views.contact_engineer_list, name='contact-engineer-list'),
    path('send/contact', views.contact_form, name='send-contact'),
    path('contact/detail/<int:pk>', views.contact_form_detail, name='contact-detail'),
    path('contact/list', views.contact_list_detail, name='contact-list'),
    path('get/service', views.get_Services, name='get-service'),
    path('do-survey', views.perform_survey, name='do-survey'),
    path('service-types', views.services_type, name='services-types'),
    path('survey-list', views.servey_list, name='survey-list'),
    path('survey-detail/<int:pk>', views.survey_detail, name='survey-detail'),
    path('request-work/', views.request_work, name='request-work'),
    path('request-work/detail/<int:pk>', views.request_work_detail, name='request_work-detail'),
    path('request-work/list', views.request_work_list, name='request-work-list'),

]
