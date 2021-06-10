from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm

from . import models


class MasterAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = \
            mark_safe(
                """
                <span style="color:red; font-size:14px;">
                    Рекомендуемый размер изображения: Ширина - 810 пикселов | 
                    Высота 1080 пикселов
                </span>
                """)

    about_master = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Master
        fields = '__all__'


@admin.register(models.Master)
class MasterAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'get_image')
    list_display_links = ('name', 'get_image')
    form = MasterAdminForm

    def get_image(self, obj):
        """Возвращает фото мастера"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return '-'

    get_image.short_description = 'Фото'

    class Meta:
        model = models.Master
        fields = '__all__'


admin.site.register(models.WorksTattooMasters)
