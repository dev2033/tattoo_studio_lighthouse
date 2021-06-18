from django.contrib import admin, messages
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm

from . import models


class MasterAdminAdminForm(ModelForm):

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


class MasterSkillsAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].help_text = \
            mark_safe(
                """
                <span style="color:white; font-size:12px;">
                    Например: название категории татуировки - Блекворк, Олд-скул.
                </span>
                """)
        self.fields['value'].help_text = \
            mark_safe(
                """
                <span style="color:white; font-size:12px;">
                    Максимально значение 100 процентов!
                </span>
                """)

    class Meta:
        model = models.MasterSkills
        fields = '__all__'


@admin.register(models.Master)
class MasterAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'get_image')
    list_display_links = ('name', 'get_image')
    form = MasterAdminAdminForm

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


@admin.register(models.MasterSkills)
class MasterSkillsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'value')
    form = MasterSkillsAdminForm

    # def add_view(self, request, form_url='', extra_context=None):
    #     for item in self.model.objects.all():
    #         if item.value >= 100:
    #             self.message_user(
    #                 request,
    #                 'Максимальное значение - 100 %',
    #                 messages.ERROR
    #             )
    #             continue
    #         else:
    #             return super().add_view(request, form_url, extra_context)

    class Meta:
        model = models.MasterSkills
        fields = '__all__'
