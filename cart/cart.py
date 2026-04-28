from django.conf import settings


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})
        if not isinstance(cart, dict):
            cart = {}
        self.cart = cart

    def __len__(self):
        return sum(item.get('quantity', 0) for item in self.cart.values())

    def __iter__(self):
        for item in self.cart.values():
            yield item

    @property
    def total(self):
        from catalog.models import Product
        total = 0
        for item in self.cart.values():
            product = Product.objects.filter(pk=item['product_id']).first()
            if product:
                price = product.current_price
                total += price * item['quantity']
        return total

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_id': product.id,
                'name': product.name,
                'quantity': 0,
                'price': str(product.current_price),
            }
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]['quantity'] = quantity
            else:
                del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def get_items(self):
        from catalog.models import Product
        items = []
        for item in self.cart.values():
            product = Product.objects.filter(pk=item['product_id']).first()
            if product:
                items.append({
                    'product': product,
                    'quantity': item['quantity'],
                    'unit_price': product.current_price,
                    'subtotal': product.current_price * item['quantity'],
                })
        return items