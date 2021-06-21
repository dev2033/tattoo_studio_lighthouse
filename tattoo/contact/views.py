from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
import requests

from .forms import ContactForm
from master.models import Master
from .models import ContactModel


class ContactView(View):
    def get(self, request):
        form = ContactForm(request.POST or None)
        return render(request, 'contact/contact.html', {'form': form})


class ContactSendView(View):
    """Отправляет сообщение из контактной формы в Telegram администраторам"""
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            appeal = form.save(commit=False)
            appeal.name = form.cleaned_data['name']
            appeal.telegram_username = form.cleaned_data['telegram_username']
            appeal.message = form.cleaned_data['message']

            masters = Master.objects.all()
            for master in masters:
                for _id in master.telegram_id.all():
                    requests.get(f'https://api.telegram.org/bot{settings.TOKEN_BOT}'
                                 f'/sendmessage?chat_id={_id}&text={appeal.name}\n'
                                 f'{appeal.telegram_username}\n{appeal.message}')

            appeal.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/contact/')
