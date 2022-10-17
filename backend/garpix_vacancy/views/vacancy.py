from django.views.generic import DetailView, ListView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Vacancy
from ..serializers import VacancySerializer


class VacancyApiView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Vacancy.active_objects.all()
    serializer_class = VacancySerializer


class VacancyListView(ListView):
    queryset = Vacancy.active_objects.all()
    context_object_name = 'vacancies'
    template_name = 'vacancies.html'


class VacancyView(DetailView):
    queryset = Vacancy.active_objects.all()
    template_name = 'vacancy.html'
