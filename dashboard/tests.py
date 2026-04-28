from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from dashboard.mixins import StaffRequiredMixin
from orders.models import Order
from catalog.models import Category, Product

User = get_user_model()


class StaffRequiredMixinTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='admin@email.com',
            email='admin@email.com',
            password='admin123',
            is_staff=True,
        )
        self.non_staff_user = User.objects.create_user(
            username='user@email.com',
            email='user@email.com',
            password='user123',
            is_staff=False,
        )

    def test_staff_user_can_access_dashboard(self):
        self.client.login(username='admin@email.com', password='admin123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_non_staff_user_gets_403(self):
        self.client.login(username='user@email.com', password='user123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_user_redirected_to_login(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)


class OrderStatusUpdateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='admin@email.com',
            email='admin@email.com',
            password='admin123',
            is_staff=True,
        )
        self.category = Category.objects.create(name='Bolos')
        self.order = Order.objects.create(
            customer_name='João Silva',
            customer_email='joao@email.com',
            customer_phone='11999999999',
            status='received',
        )

    def test_update_order_status(self):
        self.client.login(username='admin@email.com', password='admin123')
        response = self.client.post(f'/dashboard/pedidos/{self.order.pk}/status/', {
            'status': 'preparing',
        })
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'preparing')

    def test_update_order_status_invalid_status(self):
        self.client.login(username='admin@email.com', password='admin123')
        response = self.client.post(f'/dashboard/pedidos/{self.order.pk}/status/', {
            'status': 'invalid_status',
        })
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'received')

    def test_non_staff_cannot_update_status(self):
        non_staff_user = User.objects.create_user(
            username='user@email.com',
            email='user@email.com',
            password='user123',
            is_staff=False,
        )
        self.client.login(username='user@email.com', password='user123')
        response = self.client.post(f'/dashboard/pedidos/{self.order.pk}/status/', {
            'status': 'preparing',
        })
        self.assertEqual(response.status_code, 403)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'received')
