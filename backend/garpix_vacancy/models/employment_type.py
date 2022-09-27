from django.db import models
from django.utils.translation import ugettext as _


class EmploymentType(models.Model):
    type_title = models.CharField(max_length=128, verbose_name=_('Название типа'))

    def __str__(self):
        return self.type_title

    class Meta:
        verbose_name = _('Тип занятости')
        verbose_name_plural = _('Типы занятости')
