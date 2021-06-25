from django.db.models import F
from django.shortcuts import render
from django.views.generic import View, ListView

from .models import InformationBlock


class HomeView(ListView):
    """Выводит главную страницу"""
    model = InformationBlock
    context_object_name = 'blocks'
    template_name = 'about/home.html'


class AboutView(ListView):
    """Выводит страницу О нас"""
    model = InformationBlock
    context_object_name = 'about'
    template_name = 'about/about.html'
