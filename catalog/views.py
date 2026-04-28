from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_slug = self.request.GET.get('categoria')
        if categoria_slug:
            queryset = queryset.filter(category__slug=categoria_slug)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_active=True)
    slug_field = 'slug'
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'