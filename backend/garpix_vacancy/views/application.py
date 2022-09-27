from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models.application import VacancyApplication
from ..serializers.application import VacancyApplicationSerializer


class VacancyApplicationView(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = VacancyApplication.objects.all()
    serializer_class = VacancyApplicationSerializer
