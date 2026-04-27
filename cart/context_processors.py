from .cart import Cart


def cart(request):
    cart_obj = Cart(request)
    return {'cart_count': len(cart_obj)}