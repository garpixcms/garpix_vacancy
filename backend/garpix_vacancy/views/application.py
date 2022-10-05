from django.views.generic import DetailView, ListView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models.application import VacancyApplication
from ..serializers.application import VacancyApplicationSerializer


class VacancyApplicationApiView(RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = VacancyApplication.objects.all()
    serializer_class = VacancyApplicationSerializer


class VacancyApplicationView(DetailView):
    queryset = VacancyApplication.objects.all()

    template_name = 'vacancy_application.html'


class VacancyApplicationListView(ListView):
    queryset = VacancyApplication.objects.all()
    context_object_name = 'applications'
    template_name = 'vacancy_applications.html'
