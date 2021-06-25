from django.db import models


class InformationBlock(models.Model):
    """Класс модели для информации на главной странице"""
    name = models.CharField('Название блока', max_length=80)
    description = models.TextField('Описание блока')
    views = models.IntegerField('Количество посещений', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
        ordering = ["-name"]
