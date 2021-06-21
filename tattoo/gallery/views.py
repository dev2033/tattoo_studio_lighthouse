from django.views.generic import ListView

from .models import Gallery, CategoryTattoo


class GalleryView(ListView):

    model = Gallery
    context_object_name = 'gallery'
    template_name = 'gallery/gallery.html'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryTattoo.objects.all()
        return context
