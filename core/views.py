from django.views.generic import TemplateView
from catalog.models import Product, Category


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(
            is_featured=True, is_active=True
        )[:4]
        context['categories'] = Category.objects.filter(is_active=True)
        return context