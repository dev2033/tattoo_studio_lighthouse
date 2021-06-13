from django.db import models


class ContactModel(models.Model):
    """Класс модели обратной связи"""
    name = models.CharField('Имя', max_length=50)
    telegram_id = models.CharField('Телеграм ID', max_length=15)
    message = models.TextField('Текст сообщения', max_length=500)

    def __str__(self):
        return f'{self.name} - {self.telegram_id}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["-name"]
