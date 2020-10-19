from django.contrib import admin
from .models import Design, Service, Contact, RequestMeasurement, RequestWork ,Survey

admin.site.register(RequestWork)
admin.site.register(Design)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(RequestMeasurement)
admin.site.register(Survey)
