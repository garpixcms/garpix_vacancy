from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework import serializers


TagModel = import_string(getattr(settings, 'GARPIX_VACANCY_TAG_MODEL', 'garpix_vacancy.models.Tag'))


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagModel
        fields = '__all__'
