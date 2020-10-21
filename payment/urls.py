from django.urls import path
from . import views

urlpatterns = [
    path('request-type', views.get_request, name='choose-request'),
    path('create/req-measure', views.create_req_measure, name='create-req-measure'),
    path('request/detail/<int:pk>', views.req_measure_detail, name='request-measure-detail'),
    path('request/list', views.req_measure_list, name='request-measure-list'),

]
