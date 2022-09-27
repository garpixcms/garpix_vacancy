from django.contrib import admin
from ..models.employment_type import EmploymentType


@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    pass
