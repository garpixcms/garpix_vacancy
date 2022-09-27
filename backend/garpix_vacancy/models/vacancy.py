from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.module_loading import import_string
from django.utils.translation import ugettext as _
from garpix_utils.models import ActiveMixin

from .employment_type import EmploymentType
from .contact import Contact


TagModel = import_string(getattr(settings, 'GARPIX_VACANCY_TAG_MODEL', 'garpix_vacancy.models.Tag'))


class Vacancy(ActiveMixin, models.Model):
    position = models.CharField(max_length=300, blank=True, verbose_name=_('Должность'))
    city = models.CharField(max_length=300, blank=True, verbose_name=_('Город'))
    salary = models.CharField(max_length=300, blank=True, help_text=_('Пример: от 95 000 руб.'),
                              verbose_name=_('Зарплата'))
    short_description = models.CharField(max_length=1000, blank=True, verbose_name=_('Краткое описание'))
    requirements = RichTextUploadingField(blank=True, verbose_name=_('Требования'))
    conditions = RichTextUploadingField(blank=True, verbose_name=_('Условия'))
    full_name = models.CharField(max_length=100, blank=True, verbose_name=_('ФИО интервюера'))
    description = RichTextUploadingField(blank=True, verbose_name=_('Описание'))

    employment_types = models.ManyToManyField(EmploymentType, blank=False, verbose_name=_('Тип занятости'))

    contacts = models.ManyToManyField(Contact, blank=False, verbose_name=_('Контакты'))

    tags = models.ManyToManyField(TagModel, blank=True, verbose_name=_('Теги'))

    objects = models.Manager()

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
