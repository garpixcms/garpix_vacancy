from django.contrib import admin
from ..models.contact import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
