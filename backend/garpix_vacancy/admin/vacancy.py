from django.conf import settings
from django.contrib import admin

from ..models.application import VacancyApplication
from ..models.tag import Tag
from ..models.vacancy import Vacancy


if getattr(settings, 'GARPIX_VACANCY_TAG_MODEL', 'garpix_vacancy.models.Tag') == 'garpix_vacancy.models.Tag':
    @admin.register(Tag)
    class TagAdmin(admin.ModelAdmin):
        pass


class VacancyApplicationInline(admin.TabularInline):
    model = VacancyApplication
    extra = 0


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    filter_horizontal = ['contacts', 'employment_types', 'tags']
    inlines = [VacancyApplicationInline]
