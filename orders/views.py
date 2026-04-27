from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect


class CheckoutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = 'CheckoutForm'
    success_url = reverse_lazy('orders:success')


class OrderSuccessView(DetailView):
    template_name = 'orders/order_success.html'


class OrderHistoryView(ListView):
    template_name = 'orders/order_history.html'


class OrderDetailView(DetailView):
    template_name = 'orders/order_detail.html'