from django.db import models
from accounts.models import User


class Contact(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='العنوان')
    message = models.TextField(blank=True, null=True, verbose_name='الرساله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'العمل '
        verbose_name_plural = 'الأعمال '

    def __str__(self):
        return self.title


class Work(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='الأسم')
    description = models.TextField(verbose_name='الوصف', blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'العمل '
        verbose_name_plural = 'الأعمال '

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='الأسم')
    description = models.TextField(verbose_name='الوصف', blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, verbose_name='التصميمات')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'الخدمه'
        verbose_name_plural = 'الخدمات'

    def __str__(self):
        return self.name


class RequestWork(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='الأسم')
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, unique=False)
    photo = models.ImageField(verbose_name='صورة الموقع', blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, verbose_name='العنوان', blank=True, null=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'طلب عمل'
        verbose_name_plural = 'طلبات عمل'

    def __str__(self):
        return self.name


class ContactEngineer(models.Model):
    engineer_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='اسم المهندس', null=True)
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='العنوان')
    message = models.TextField(blank=True, null=True, verbose_name='الرساله')
    sender_email = models.EmailField(blank=True, max_length=254, verbose_name='البريد الألكترونى الخاص بالمرسل',
                                     null=True)
    sender_name = models.CharField(max_length=255, verbose_name='اسم المرسل', null=True, blank=True)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'المرسل'
        verbose_name_plural = 'المرسلات'

    def __str__(self):
        return self.title


class Reply(models.Model):
    customer = models.ForeignKey(User, null=True, related_name='العميل', on_delete=models.CASCADE)
    reply_message = models.TextField(blank=True, null=True, verbose_name='الأجابه')

    class Meta:
        ordering = ['reply_message', ]
        verbose_name = 'الرد'
        verbose_name_plural = 'الردود'

    def __str__(self):
        return self.reply_message


class RequestMeasurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='العميل')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='الخدمه')
    description = models.TextField(blank=True, null=True, verbose_name='الوصف')

    class Meta:
        ordering = ['user', ]
        verbose_name = 'طلب مقايسه'
        verbose_name_plural = ' طلبات مقايسه'

    def __str__(self):
        return self.address


class Survey(models.Model):
    color = models.CharField(max_length=255, null=True, blank=True, verbose_name='اللون المفضل')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='العميل')
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, verbose_name='نوع الخدمه')
    interests = models.CharField(max_length=255, null=True, blank=True, verbose_name='الاهتمامات')
    quote = models.CharField(max_length=255, null=True, blank=True, verbose_name='نبذه')

    class Meta:
        ordering = ['color', ]
        verbose_name = 'استطلاع رأى'
        verbose_name_plural = 'استطلاعات الرأى'

    def __str__(self):
        return self.color
