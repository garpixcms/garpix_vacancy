from django.db import models
from django.utils.translation import ugettext as _


class ContactType(models.Model):
    type_title = models.CharField(max_length=128, verbose_name=_('Название типа'))

    def __str__(self):
        return self.type_title

    class Meta:
        verbose_name = _('Тип контакта')
        verbose_name_plural = _('Типы контактов')


class Contact(models.Model):
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE, related_name='contacts', verbose_name=_('Тип контакта'))
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('ФИО контактного лица'))
    contact_value = models.CharField(max_length=255, verbose_name=_('Контакт'))

    def __str__(self):
        return self.contact_person if self.contact_person else self.contact_value

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')
