from django.contrib import admin
from ..models.application import VacancyApplication


@admin.register(VacancyApplication)
class VacancyApplicationAdmin(admin.ModelAdmin):
    pass
