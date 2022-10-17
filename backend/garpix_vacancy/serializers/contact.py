from rest_framework import serializers
from ..models import Contact


class ContactSerializer(serializers.ModelSerializer):
    contact_type = serializers.CharField(source='contact_type.type_title')

    class Meta:
        model = Contact
        fields = ('id', 'contact_value', 'contact_type')
