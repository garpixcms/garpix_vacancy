from django.contrib import admin
from ..models.contact import Contact, ContactType


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
