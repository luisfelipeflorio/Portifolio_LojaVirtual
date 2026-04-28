from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from catalog.models import Product
from .cart import Cart


class CartDetailView(View):
    template_name = 'cart/detail.html'

    def get(self, request):
        cart = Cart(request)
        cart_items = cart.get_items()
        cart_total = cart.total
        return render(request, self.template_name, {
            'cart_items': cart_items,
            'cart_total': cart_total,
        })


class CartAddView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        product = Product.objects.filter(pk=product_id, is_active=True).first()
        if not product:
            messages.error(request, 'Produto não encontrado.')
            return redirect('catalog:list')

        cart = Cart(request)
        cart.add(product, quantity)
        messages.success(request, f'{product.name} adicionado ao carrinho!')
        return redirect('cart:detail')


class CartRemoveView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        cart = Cart(request)
        cart.remove(product_id)
        messages.success(request, 'Produto removido do carrinho!')
        return redirect('cart:detail')


class CartUpdateView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = Cart(request)
        cart.update(product_id, quantity)
        messages.success(request, 'Carrinho atualizado!')
        return redirect('cart:detail')


class CartAddAjaxView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        product = Product.objects.filter(pk=product_id, is_active=True).first()
        if not product:
            return JsonResponse({'success': False, 'message': 'Produto não encontrado.'})

        cart = Cart(request)
        cart.add(product, quantity)

        return JsonResponse({
            'success': True,
            'message': f'{product.name} adicionado ao carrinho!',
            'cart_count': len(cart),
        })