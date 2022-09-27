from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework import serializers

from .contact import ContactSerializer
from .employment_type import EmploymentTypeSerializer
from ..models import Vacancy


TagModel = import_string(getattr(settings, 'GARPIX_VACANCY_TAG_MODEL', 'garpix_vacancy.models.Tag'))


class VacancySerializer(serializers.ModelSerializer):

    contacts = ContactSerializer(many=True)
    employment_types = EmploymentTypeSerializer(many=True)
    tags = TagModel.get_serializer()(many=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'position', 'city', 'salary', 'short_description', 'requirements', 'conditions', 'full_name',
                  'description', 'contacts', 'employment_types', 'tags')
