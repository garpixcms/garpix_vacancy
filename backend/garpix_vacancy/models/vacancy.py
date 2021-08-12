from django.db import models
from django.conf import settings
from django.utils.module_loading import import_string
from ckeditor_uploader.fields import RichTextUploadingField
from .contact import Contact

VacancyMixin = import_string(settings.GARPIX_VACANCY_MIXIN)


class Vacancy(VacancyMixin, models.Model):
    position = models.CharField(max_length=300, verbose_name='Должность', blank=True, null=True)
    city = models.CharField(max_length=300, verbose_name='Город', blank=True, null=True)
    salary = models.CharField(max_length=300, verbose_name='Зарплата', blank=True, null=True,
                              help_text='Пример: от 95 000 руб.')
    short_description = models.CharField(max_length=1000, verbose_name='Краткое описание', blank=True, null=True)
    requirements = RichTextUploadingField(verbose_name='Требования', blank=True, null=True)
    conditions = RichTextUploadingField(verbose_name='Условия', blank=True, null=True)
    full_name = models.CharField(max_length=100, verbose_name='ФИО интервьюера', blank=True, null=True)
    description = RichTextUploadingField(blank=True, verbose_name='Описание', null=True)
    contacts = models.ForeignKey(Contact, on_delete=models.SET_NULL, verbose_name='Контакты', blank=True, null=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
