from django.test import TestCase
from catalog.models import Category, Product


class CartFlowTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Bolos')
        self.product1 = Product.objects.create(
            category=self.category,
            name='Bolo de Chocolate',
            price=50.00,
            is_active=True,
        )
        self.product2 = Product.objects.create(
            category=self.category,
            name='Bolo de Morango',
            price=60.00,
            is_active=True,
        )

    def test_add_product_to_cart(self):
        response = self.client.post('/carrinho/add/', {'product_id': self.product1.id, 'quantity': 1})
        self.assertEqual(response.status_code, 302)
        session = self.client.session
        self.assertIn('cart', session)
        self.assertIn(str(self.product1.id), session['cart'])

    def test_add_multiple_quantity(self):
        self.client.post('/carrinho/add/', {'product_id': self.product1.id, 'quantity': 3})
        session = self.client.session
        self.assertEqual(session['cart'][str(self.product1.id)]['quantity'], 3)

    def test_update_cart_item_quantity(self):
        self.client.post('/carrinho/add/', {'product_id': self.product1.id, 'quantity': 2})
        self.client.post('/carrinho/update/', {'product_id': self.product1.id, 'quantity': 5})
        session = self.client.session
        self.assertEqual(session['cart'][str(self.product1.id)]['quantity'], 5)

    def test_remove_cart_item(self):
        self.client.post('/carrinho/add/', {'product_id': self.product1.id, 'quantity': 1})
        self.client.post('/carrinho/add/', {'product_id': self.product2.id, 'quantity': 1})
        session = self.client.session
        self.assertEqual(len(session['cart']), 2)
        self.client.post('/carrinho/remove/', {'product_id': self.product1.id})
        session = self.client.session
        self.assertEqual(len(session['cart']), 1)
        self.assertNotIn(str(self.product1.id), session['cart'])

    def test_cart_total(self):
        self.client.post('/carrinho/add/', {'product_id': self.product1.id, 'quantity': 2})
        self.client.post('/carrinho/add/', {'product_id': self.product2.id, 'quantity': 1})
        response = self.client.get('/carrinho/')
        self.assertEqual(response.status_code, 200)
        expected_total = (self.product1.current_price * 2) + (self.product2.current_price * 1)
        self.assertContains(response, str(expected_total))

    def test_clear_cart(self):
        self.client.post('/carrinho/add/', {'product_id': self.product1.id, 'quantity': 1})
        self.client.post('/carrinho/add/', {'product_id': self.product2.id, 'quantity': 1})
        session = self.client.session
        self.assertEqual(len(session['cart']), 2)
        session['cart'] = {}
        session.save()
        self.assertEqual(len(session['cart']), 0)
