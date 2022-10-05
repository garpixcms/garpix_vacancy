from django.conf import settings
from django.urls import re_path, path, include
from . import views

from rest_framework_nested import routers


app_name = 'garpix_vacancy'

API_URL = getattr(settings, 'API_URL', 'api')

urlpatterns = [
    re_path(r'vacancy/(?P<pk>\d+)/$', views.VacancyView.as_view(), name='vacancy'),
    re_path(r'vacancy/(?P<pk>\d+)$', views.VacancyView.as_view(), name='vacancy'),
    re_path(r'vacancies/', views.VacancyListView.as_view(), name='vacancies'),
    re_path(r'vacancies', views.VacancyListView.as_view(), name='vacancies'),
    re_path(r'vacancy_application/(?P<pk>\d+)/$', views.VacancyApplicationView.as_view(), name='vacancy_application'),
    re_path(r'vacancy_application/(?P<pk>\d+)$', views.VacancyApplicationView.as_view(), name='vacancy_application'),
    re_path(r'vacancy_applications/', views.VacancyApplicationListView.as_view(), name='vacancy_applications'),
    re_path(r'vacancy_applications', views.VacancyApplicationListView.as_view(), name='vacancy_applications')
]

router = routers.SimpleRouter()

router.register(f'{API_URL}/vacancy', views.VacancyApiView, basename='api_vacancy')

domains_router = routers.NestedDefaultRouter(router, f'{API_URL}/vacancy', lookup='vacancy')
domains_router.register(r'vacancy_application', views.VacancyApplicationApiView, basename='api_vacancy_application')

urlpatterns += [
    path(r'', include(router.urls)),
    path(r'', include(domains_router.urls)),
]
