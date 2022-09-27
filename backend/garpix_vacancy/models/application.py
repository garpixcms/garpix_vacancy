from django.db import models
from django.utils.translation import ugettext as _

from .vacancy import Vacancy
from garpix_utils.file import get_file_path


class VacancyApplication(models.Model):

    full_name = models.CharField(max_length=255, verbose_name=_('ФИО'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Номер телефона'))
    email = models.EmailField(verbose_name=_('Email'))
    extra_info = models.TextField(blank=True, null=True, verbose_name=_('Дополнительная информация'))
    cv_file = models.FileField(upload_to=get_file_path, blank=True, null=True, verbose_name=_('Файл'))
    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, null=True, related_name='applications', verbose_name=_('Вакансия'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Отклик на вакансию')
        verbose_name_plural = _('Отклики на вакансии')
