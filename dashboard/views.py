from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class StaffRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Acesso restrito a administradores.")
        return super().dispatch(request, *args, **kwargs)


class DashboardHomeView(StaffRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'


class ProductListView(StaffRequiredMixin, ListView):
    template_name = 'dashboard/product_list.html'


class ProductCreateView(StaffRequiredMixin, CreateView):
    template_name = 'dashboard/product_form.html'


class ProductUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'dashboard/product_form.html'


class ProductDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'dashboard/product_confirm_delete.html'


class CategoryListView(StaffRequiredMixin, ListView):
    template_name = 'dashboard/category_list.html'


class CategoryCreateView(StaffRequiredMixin, CreateView):
    template_name = 'dashboard/category_form.html'


class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'dashboard/category_form.html'


class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'dashboard/category_confirm_delete.html'


class OrderListView(StaffRequiredMixin, ListView):
    template_name = 'dashboard/order_list.html'


class OrderDetailView(StaffRequiredMixin, DetailView):
    template_name = 'dashboard/order_detail.html'


class OrderStatusUpdateView(StaffRequiredMixin, View):
    pass