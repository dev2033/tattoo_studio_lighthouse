from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import InformationBlock, Category, Article


class HomeView(ListView):
    """Выводит главную страницу"""
    model = InformationBlock
    context_object_name = 'blocks'
    template_name = 'about/home.html'
    # def get(self, request, *args, **kwargs):
    #     blocks = InformationBlock.objects.all()
    #     # articles = Article.objects.select_related('category').get(slug=self.kwargs.get('slug'))
    #     print(articles.category)
    #     # for a in articles:
    #     #     print(a.name)
    #
    #     return render(request, 'about/home.html', {'blocks': blocks, 'category': articles})


class AboutView(ListView):
    """Выводит страницу О нас"""
    queryset = Article.objects.all()
    context_object_name = 'articles'
    template_name = 'about/about.html'


# class ArticlesDetail(DetailView):
#     """Выводит полностью статью"""

