from django.session import SessionBase


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
        return iter(self.cart.values())