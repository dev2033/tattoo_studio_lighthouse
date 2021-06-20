import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, View, CreateView

from contact.models import AdminTelegramId
from .forms import RecordToMasterForm
from .models import Master


class MastersListView(ListView):
    """Выводит список мастеров"""
    model = Master
    context_object_name = 'masters'
    template_name = 'master/masters_list.html'


class MasterDetailView(DetailView):
    """Выводит информацию о конкретном мастере"""
    model = Master
    context_object_name = 'master'
    template_name = 'master/master_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        master = context['master']
        context['skills'] = master.master_skills.all()
        context['form'] = RecordToMasterForm(self.request.POST or None)
        return context


class RecordToMaster(CreateView):
    """Запись на сеанс к мастеру"""
    model = Master
    form_class = RecordToMasterForm

    def form_valid(self, form):
        form.instance.master_id = self.kwargs.get('pk')
        master = Master.objects.get(id=form.instance.master_id)
        master_telegram_id = master.telegram_id.all()
        client = form.save(commit=False)
        client.name = form.instance.name
        client.telegram_username = form.instance.telegram_username
        client.message = form.instance.message

        for tg_id in master_telegram_id:
            requests.get(f'https://api.telegram.org/bot{settings.TOKEN_BOT}'
                         f'/sendmessage?chat_id={tg_id}&text={client.name}\n'
                         f'{client.telegram_username}\n{client.message}')

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.master.get_absolute_url()

