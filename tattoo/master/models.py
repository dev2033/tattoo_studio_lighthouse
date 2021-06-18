from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator


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


class MasterSkills(models.Model):
    """Умения мастера"""
    name = models.CharField('Название', max_length=50)
    value = models.PositiveSmallIntegerField(
        verbose_name='Значение (%)',
        default=1,
        validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Умение мастера"
        verbose_name_plural = "Умения мастера"
        ordering = ["name"]
