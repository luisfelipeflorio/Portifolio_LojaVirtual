from django.test import TestCase
from django.conf import settings
from django.test import Client
from orders.models import Order, OrderItem


class OrderGenerateProtocolTest(TestCase):
    def test_protocol_generated_on_save(self):
        order = Order.objects.create(
            customer_name='João Silva',
            customer_email='joao@email.com',
            customer_phone='11999999999',
        )
        self.assertIsNotNone(order.protocol)
        self.assertTrue(order.protocol.startswith('CON-'))

    def test_protocol_is_unique(self):
        order1 = Order.objects.create(
            customer_name='João Silva',
            customer_email='joao@email.com',
            customer_phone='11999999999',
        )
        order2 = Order.objects.create(
            customer_name='Maria Santos',
            customer_email='maria@email.com',
            customer_phone='11888888888',
        )
        self.assertNotEqual(order1.protocol, order2.protocol)

    def test_protocol_format(self):
        order = Order.objects.create(
            customer_name='João Silva',
            customer_email='joao@email.com',
            customer_phone='11999999999',
        )
        self.assertRegex(order.protocol, r'^CON-\d{4}\d{4}$')


class OrderItemSubtotalTest(TestCase):
    def setUp(self):
        from catalog.models import Category, Product
        self.category = Category.objects.create(name='Bolos')
        self.product = Product.objects.create(
            category=self.category,
            name='Bolo de Chocolate',
            price=50.00,
        )
        self.order = Order.objects.create(
            customer_name='João Silva',
            customer_email='joao@email.com',
            customer_phone='11999999999',
        )

    def test_subtotal_calculated_on_save(self):
        item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            product_name=self.product.name,
            unit_price=50.00,
            quantity=3,
        )
        self.assertEqual(item.subtotal, 150.00)

    def test_subtotal_updated_when_quantity_changes(self):
        item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            product_name=self.product.name,
            unit_price=50.00,
            quantity=2,
        )
        item.quantity = 5
        item.save()
        self.assertEqual(item.subtotal, 250.00)


class CheckoutFlowTest(TestCase):
    def setUp(self):
        from catalog.models import Category, Product
        self.client = Client()
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

    def test_valid_checkout_creates_order_and_items(self):
        session = self.client.session
        session['cart'] = {
            str(self.product1.id): {
                'product_id': self.product1.id,
                'name': self.product1.name,
                'quantity': 2,
                'price': str(self.product1.current_price),
            },
            str(self.product2.id): {
                'product_id': self.product2.id,
                'name': self.product2.name,
                'quantity': 1,
                'price': str(self.product2.current_price),
            },
        }
        session.save()

        response = self.client.post('/pedido/', {
            'customer_name': 'João Silva',
            'customer_email': 'joao@email.com',
            'customer_phone': '11999999999',
            'delivery_type': 'pickup',
            'delivery_address': '',
            'scheduled_at': '',
            'notes': '',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.exists())
        order = Order.objects.first()
        self.assertEqual(order.customer_name, 'João Silva')
        self.assertEqual(order.items.count(), 2)
        self.assertEqual(order.subtotal, (self.product1.current_price * 2) + (self.product2.current_price * 1))

    def test_checkout_with_empty_cart_shows_error(self):
        response = self.client.post('/pedido/', {
            'customer_name': 'João Silva',
            'customer_email': 'joao@email.com',
            'customer_phone': '11999999999',
            'delivery_type': 'pickup',
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Order.objects.exists())
