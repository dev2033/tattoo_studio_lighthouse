from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms

from . import models


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    description.label = 'Описание'

    class Meta:
        model = models.InformationBlock
        fields = '__all__'


@admin.register(models.InformationBlock)
class InfoAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'views')
    list_display_links = ('id', 'name')


admin.site.site_title = 'Административная панель сайта Тату-студии "Якорь"'
admin.site.site_header = 'Административная панель сайта Тату-студии "Якорь"'
