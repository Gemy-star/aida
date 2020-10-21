from django.contrib import admin
from .models import Service, Contact, RequestMeasurement, RequestWork, Survey, ContactEngineer

admin.site.register(RequestWork)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(RequestMeasurement)
admin.site.register(Survey)
admin.site.register(ContactEngineer)
