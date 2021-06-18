from django.views.generic import ListView, DetailView

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
