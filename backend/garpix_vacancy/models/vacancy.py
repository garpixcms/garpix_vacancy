from django.db import models
from django.conf import settings
from django.utils.module_loading import import_string
from ckeditor_uploader.fields import RichTextUploadingField
from .contact import Contact

VacancyMixin = import_string(settings.GARPIX_VACANCY_MIXIN)


class Vacancy(VacancyMixin, models.Model):
    position = models.CharField(max_length=300, verbose_name='Должность', blank=True)
    city = models.CharField(max_length=300, verbose_name='Город', blank=True)
    salary = models.CharField(max_length=300, verbose_name='Зарплата', blank=True, help_text='Пример: от 95 000 руб.')
    short_description = models.CharField(max_length=1000, verbose_name='Краткое описание', blank=True)
    requirements = RichTextUploadingField(verbose_name='Требования', blank=True)
    conditions = RichTextUploadingField(verbose_name='Условия', blank=True)
    full_name = models.CharField(max_length=100, verbose_name='ФИО интервьюера', blank=True)
    description = RichTextUploadingField(blank=True, verbose_name='Описание')
    contacts = models.ForeignKey(Contact, on_delete=models.SET_NULL, verbose_name='Контакты', blank=True, null=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
