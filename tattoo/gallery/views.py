from django.views.generic import ListView

from .models import Gallery, CategoryTattoo


class GalleryView(ListView):
    queryset = CategoryTattoo.objects.prefetch_related('gallery_category')
    context_object_name = 'categories'
    template_name = 'gallery/gallery.html'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        a = CategoryTattoo.objects.prefetch_related('gallery_category')

        return context
