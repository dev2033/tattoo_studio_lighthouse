from django.contrib import admin

from .models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_id')
    list_display_links = ('name', 'telegram_id')
