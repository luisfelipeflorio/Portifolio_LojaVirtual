from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count, Sum, Q
from datetime import datetime, timedelta

from .mixins import StaffRequiredMixin
from catalog.models import Product, Category
from orders.models import Order
from orders.signals import send_status_update_email


class DashboardHomeView(StaffRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        today_start = timezone.make_aware(datetime.combine(today, datetime.min.time()))
        today_end = timezone.make_aware(datetime.combine(today, datetime.max.time()))

        context['orders_today'] = Order.objects.filter(created_at__range=(today_start, today_end)).count()
        context['revenue_today'] = Order.objects.filter(
            created_at__range=(today_start, today_end)
        ).aggregate(total=Sum('total'))['total'] or 0

        context['pending_orders'] = Order.objects.filter(
            Q(status='received') | Q(status='preparing')
        ).count()

        context['ready_orders'] = Order.objects.filter(status='ready').count()
        context['recent_orders'] = Order.objects.all()[:10]

        return context


class CategoryListView(StaffRequiredMixin, ListView):
    model = Category
    template_name = 'dashboard/category_list.html'
    context_object_name = 'categories'
    ordering = ['sort_order', 'name']


class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    template_name = 'dashboard/category_form.html'
    fields = ['name', 'description', 'image', 'is_active', 'sort_order']
    success_url = reverse_lazy('dashboard:category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Categoria criada com sucesso!')
        return super().form_valid(form)


class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    model = Category
    template_name = 'dashboard/category_form.html'
    fields = ['name', 'description', 'image', 'is_active', 'sort_order']
    success_url = reverse_lazy('dashboard:category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Categoria atualizada com sucesso!')
        return super().form_valid(form)


class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    model = Category
    template_name = 'dashboard/category_confirm_delete.html'
    success_url = reverse_lazy('dashboard:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Categoria excluída com sucesso!')
        return super().delete(request, *args, **kwargs)


class ProductListView(StaffRequiredMixin, ListView):
    model = Product
    template_name = 'dashboard/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = Product.objects.all()
        category = self.request.GET.get('categoria')
        status = self.request.GET.get('status')

        if category:
            qs = qs.filter(category_id=category)
        if status == 'active':
            qs = qs.filter(is_active=True)
        elif status == 'inactive':
            qs = qs.filter(is_active=False)
        elif status == 'featured':
            qs = qs.filter(is_featured=True)
        elif status == 'promotion':
            qs = qs.filter(is_promotion=True)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        return context


class ProductCreateView(StaffRequiredMixin, CreateView):
    model = Product
    template_name = 'dashboard/product_form.html'
    fields = ['category', 'name', 'description', 'price', 'image', 'is_active',
              'is_featured', 'is_promotion', 'promotion_price', 'stock']
    success_url = reverse_lazy('dashboard:product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Produto criado com sucesso!')
        return super().form_valid(form)


class ProductUpdateView(StaffRequiredMixin, UpdateView):
    model = Product
    template_name = 'dashboard/product_form.html'
    fields = ['category', 'name', 'description', 'price', 'image', 'is_active',
              'is_featured', 'is_promotion', 'promotion_price', 'stock']
    success_url = reverse_lazy('dashboard:product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return super().form_valid(form)


class ProductDeleteView(StaffRequiredMixin, DeleteView):
    model = Product
    template_name = 'dashboard/product_confirm_delete.html'
    success_url = reverse_lazy('dashboard:product_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Produto excluído com sucesso!')
        return super().delete(request, *args, **kwargs)


class OrderListView(StaffRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get('status')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        if status:
            qs = qs.filter(status=status)
        if date_from:
            qs = qs.filter(created_at__date__gte=date_from)
        if date_to:
            qs = qs.filter(created_at__date__lte=date_to)

        return qs


class OrderDetailAdminView(StaffRequiredMixin, DetailView):
    model = Order
    template_name = 'dashboard/order_detail.html'
    context_object_name = 'order'


class OrderStatusUpdateView(StaffRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        new_status = request.POST.get('status')

        if new_status in dict(Order.STATUS_CHOICES):
            old_status = order.status
            order.status = new_status
            order.save()

            if old_status != new_status:
                send_status_update_email(order)

            messages.success(request, f'Status do pedido {order.protocol} atualizado para {dict(Order.STATUS_CHOICES)[new_status]}.')

        return HttpResponseRedirect(reverse_lazy('dashboard:order_detail', kwargs={'pk': pk}))
