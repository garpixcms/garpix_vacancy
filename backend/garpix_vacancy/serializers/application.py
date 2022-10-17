from rest_framework import serializers
from ..models.application import VacancyApplication


class VacancyApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyApplication
        fields = '__all__'
