from django.db import models
from django.utils.translation import ugettext as _


class Tag(models.Model):
    tag = models.CharField(max_length=128, verbose_name=_('Тег'))

    @classmethod
    def get_serializer(cls):
        from ..serializers.tag import TagSerializer
        return TagSerializer

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')
