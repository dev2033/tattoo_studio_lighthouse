from django.views.generic import ListView

from .models import CategoryTattoo


class GalleryView(ListView):
    queryset = CategoryTattoo.objects.prefetch_related('gallery_category')
    context_object_name = 'categories'
    template_name = 'gallery/gallery.html'
    paginate_by = 20
