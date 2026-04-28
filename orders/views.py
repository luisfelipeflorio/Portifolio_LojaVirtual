from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.cart import Cart


class CheckoutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('orders:success')

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['customer_name'] = f'{self.request.user.first_name} {self.request.user.last_name}'.strip()
            initial['customer_email'] = self.request.user.email
            initial['customer_phone'] = self.request.user.phone or ''
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart_items'] = cart.get_items()
        context['cart_total'] = cart.total
        context['cart_count'] = len(cart)
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        if len(cart) == 0:
            messages.error(self.request, 'Seu carrinho está vazio.')
            return redirect('cart:detail')

        cleaned_data = form.cleaned_data
        delivery_type = cleaned_data.get('delivery_type')
        delivery_fee = 0 if delivery_type == 'pickup' else 15.00

        order = Order.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            delivery_type=delivery_type,
            customer_name=cleaned_data['customer_name'],
            customer_email=cleaned_data['customer_email'],
            customer_phone=cleaned_data['customer_phone'],
            delivery_address=cleaned_data.get('delivery_address', ''),
            scheduled_at=cleaned_data.get('scheduled_at'),
            notes=cleaned_data.get('notes', ''),
            subtotal=cart.total,
            delivery_fee=delivery_fee,
            total=cart.total + delivery_fee,
        )

        for item in cart.get_items():
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                product_name=item['product'].name,
                unit_price=item['unit_price'],
                quantity=item['quantity'],
            )

        cart.clear()
        messages.success(self.request, f'Pedido realizado com sucesso! Protocolo: {order.protocol}')
        return redirect(reverse_lazy('orders:success') + f'?pk={order.pk}')


class OrderSuccessView(DetailView):
    template_name = 'orders/order_success.html'
    model = Order
    context_object_name = 'order'

    def get_object(self):
        pk = self.request.GET.get('pk')
        if pk:
            return get_object_or_404(Order, pk=pk)
        protocol = self.request.GET.get('protocol')
        if protocol:
            return get_object_or_404(Order, protocol=protocol)
        return None


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'orders/order_history.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'orders/order_detail.html'
    model = Order
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user and obj.user != self.request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied('Você não tem permissão para ver este pedido.')
        return obj