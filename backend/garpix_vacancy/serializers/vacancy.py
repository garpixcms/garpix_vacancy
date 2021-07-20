from rest_framework import serializers
from ..models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('position', 'city', 'salary', 'short_description', 'requirements', 'conditions', 'full_name',
                  'description', 'contacts')
