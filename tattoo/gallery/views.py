from django.shortcuts import render
from django.views.generic import View, ListView

from .models import Gallery, CategoryTattoo


class GalleryView(ListView):

    model = Gallery
    context_object_name = 'gallery'
    template_name = 'gallery/gallery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = CategoryTattoo.objects.all()
        # g = Gallery.objects.get()
        context['categories'] = categories
        print(categories)
        return context
