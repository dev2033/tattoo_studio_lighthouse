from django.db import models
from django.urls import reverse


class Master(models.Model):
    """Мастера"""
    name = models.CharField('Имя мастера', max_length=150)
    image = models.ImageField('Изображение мастера', upload_to='masters/')
    about_master = models.TextField('Информация о мастере')
    vk = models.CharField('Ссылка на ВК', max_length=255, blank=True, null=True)
    instagram = models.CharField('Ссылка на Instagram', max_length=255,
                                 blank=True, null=True)
    telegram = models.CharField('Ссылка на Telegram', max_length=255,
                                blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('master_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"
        ordering = ["name"]


class WorksTattooMasters(models.Model):
    """Работы тату-мастеров"""
    image = models.ImageField('Изображения', upload_to='works_masters/')

    def __str__(self):
        return f'{id} изображение'

    class Meta:
        verbose_name = "Работы мастеров"
        verbose_name_plural = "Работы мастеров"
        ordering = ["-id"]
