from django import forms

from .models import ContactModel


class ContactForm(forms.ModelForm):
    """Форма комментариев"""
    class Meta:
        model = ContactModel
        fields = ('name', 'telegram_id', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя', 'id': 'fname', 'name': 'fname'}),

            'telegram_id': forms.TextInput(attrs={
                'placeholder': 'Телеграм ID', 'id': 'tg_id'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Текст сообщения',
                'name': 'msg',
                'id': 'msg',
            })
        }

