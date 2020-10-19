from django.db import models
from accounts.models import User


class Design(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name')
    picture = models.ImageField(verbose_name='Design Picture', blank=True, null=True)
    engineer = models.ManyToManyField(User, verbose_name='Engineer')
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    designs = models.ManyToManyField(Design, verbose_name='Designs')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class RequestWork(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name')
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, unique=False)
    photo = models.ImageField(verbose_name='Location Picture', blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name='Address', blank=True, null=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return self.name


class Contact(models.Model):
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Engineer Contacted', null=True)
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Subject')
    message = models.TextField(blank=True, null=True, verbose_name='Message')
    sender = models.EmailField(blank=True, max_length=254, verbose_name='Sender Email', null=True)
    user_name = models.CharField(max_length=255, verbose_name='Sender Name', null=True, blank=True)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.title


class Reply(models.Model):
    engineer = models.ForeignKey(User, null=True, related_name='Engineer', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, null=True, related_name='Customer', on_delete=models.CASCADE)
    reply_message = models.TextField(blank=True, null=True, verbose_name='Reply')

    class Meta:
        ordering = ['reply_message', ]
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

    def __str__(self):
        return self.reply_message


class RequestMeasurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    class Meta:
        ordering = ['user', ]
        verbose_name = 'Request Measurement'
        verbose_name_plural = 'Request Measurements'

    def __str__(self):
        return self.address


class Survey(models.Model):
    color = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design_type = models.ForeignKey(Design, on_delete=models.CASCADE, verbose_name='Design Type')
    interests = models.CharField(max_length=255, null=True, blank=True)
    quote = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['color', ]
        verbose_name = 'Survey'
        verbose_name_plural = 'Survey'

    def __str__(self):
        return self.color


class Work(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    work_photo = models.ImageField(blank=True, null=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.name
