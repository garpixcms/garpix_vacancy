from rest_framework import serializers
from ..models import EmploymentType


class EmploymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmploymentType
        fields = '__all__'
