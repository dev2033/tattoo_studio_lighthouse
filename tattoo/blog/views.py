from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Post, Tag


class BaseView(View):
    """Выводит главную страницу"""
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


class PostsListView(ListView):
    """Выводит список постов"""
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts_list.html'
    paginate_by = 9


class PostDetail(DetailView):
    """Выводит пост отдельно"""
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class SearchPostsListView(ListView):
    """Поиск постов"""
    template_name = 'blog/search_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
