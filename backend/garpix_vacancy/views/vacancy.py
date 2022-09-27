from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Vacancy
from ..serializers import VacancySerializer


class VacancyListView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Vacancy.active_objects.all()
    serializer_class = VacancySerializer
