from django.contrib import admin
from ..models.vacancy import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
