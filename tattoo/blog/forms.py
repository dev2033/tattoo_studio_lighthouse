from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма комментариев"""
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Текст сообщения',
                'name': 'massage',
                'cols': '30',
                'rows': '10',
            })
        }
