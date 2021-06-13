from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, View
from django.conf import settings
import requests

from .forms import ContactForm


class ContactView(View):
    def get(self, request):
        form = ContactForm(request.POST or None)
        return render(request, 'contact/contact.html', {'form': form})


class ContactSendView(View):
    """Контактная форма"""
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            appeal = form.save(commit=False)
            appeal.name = form.cleaned_data['name']
            appeal.telegram_id = form.cleaned_data['telegram_id']
            appeal.message = form.cleaned_data['message']
            masters_id = ['939392408', '1768605437']
            for _id in masters_id:
                requests.post(f'https://api.telegram.org/bot{settings.TOKEN_BOT}'
                              f'/sendmessage?chat_id={_id}&text={appeal.name}\n{appeal.telegram_id}\n{appeal.message}')
            appeal.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/contact/')




    # form_class = ContactForm
    # success_url = '/'
    # template_name = 'contact/contact.html'

