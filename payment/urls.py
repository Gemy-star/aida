from django.urls import path
from . import views

urlpatterns = [
    path('service-cycle', views.service_cycle, name='tour-service'),
    path('design-cycle', views.design_cycle, name='tour-design'),
    path('engineer-cycle', views.engineer_cycle, name='tour-engineer'),
    path('final-cycle', views.final_tour, name='tour-final'),

]
