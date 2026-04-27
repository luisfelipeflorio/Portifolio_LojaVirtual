from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages


class CartDetailView(View):
    template_name = 'cart/detail.html'

    def get(self, request):
        return render(request, self.template_name)


class CartAddView(View):
    def post(self, request):
        messages.success(request, 'Produto adicionado ao carrinho!')
        return redirect('cart:detail')


class CartRemoveView(View):
    def post(self, request, product_id):
        messages.success(request, 'Produto removido do carrinho!')
        return redirect('cart:detail')


class CartUpdateView(View):
    def post(self, request, product_id):
        messages.success(request, 'Carrinho atualizado!')
        return redirect('cart:detail')