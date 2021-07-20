from django.db import models
from django.conf import settings
from django.utils.module_loading import import_string

ContactMixin = import_string(settings.GARPIX_CONTACT_MIXIN)


class Contact(ContactMixin, models.Model):
    address = models.CharField(max_length=300, verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=300, verbose_name='Телефон', blank=True)
    fio = models.CharField(max_length=300, verbose_name='ФИО', blank=True)
    email = models.CharField(max_length=300, verbose_name='Почта', blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
