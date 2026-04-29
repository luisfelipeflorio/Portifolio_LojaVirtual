from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Address

User = get_user_model()


class AddressManagementTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user@email.com',
            email='user@email.com',
            password='user123',
        )
        self.other_user = User.objects.create_user(
            username='other@email.com',
            email='other@email.com',
            password='other123',
        )
        self.client.login(username='user@email.com', password='user123')
        self.address = Address.objects.create(
            user=self.user,
            street='Rua das Flores',
            number='100',
            neighborhood='Centro',
            city='São Paulo',
            state='SP',
            zip_code='01001-000',
        )

    def test_address_list_requires_login(self):
        self.client.logout()
        response = self.client.get('/accounts/addresses/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_address_list_shows_user_addresses(self):
        response = self.client.get('/accounts/addresses/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rua das Flores')

    def test_address_list_does_not_show_other_user_addresses(self):
        Address.objects.create(
            user=self.other_user,
            street='Rua Secreta',
            number='1',
            neighborhood='Bairro',
            city='Rio de Janeiro',
            state='RJ',
            zip_code='20000-000',
        )
        response = self.client.get('/accounts/addresses/')
        self.assertNotContains(response, 'Rua Secreta')

    def test_create_address(self):
        response = self.client.post('/accounts/addresses/create/', {
            'street': 'Av. Paulista',
            'number': '1000',
            'complement': '',
            'neighborhood': 'Bela Vista',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '01310-100',
            'is_default': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Address.objects.filter(user=self.user).count(), 2)

    def test_create_address_as_default_clears_previous_default(self):
        self.address.is_default = True
        self.address.save()
        self.client.post('/accounts/addresses/create/', {
            'street': 'Av. Paulista',
            'number': '1000',
            'complement': '',
            'neighborhood': 'Bela Vista',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '01310-100',
            'is_default': True,
        })
        self.address.refresh_from_db()
        self.assertFalse(self.address.is_default)
        self.assertTrue(Address.objects.get(street='Av. Paulista').is_default)

    def test_update_address(self):
        response = self.client.post(f'/accounts/addresses/update/{self.address.pk}/', {
            'street': 'Rua das Flores Atualizada',
            'number': '200',
            'complement': '',
            'neighborhood': 'Centro',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '01001-000',
            'is_default': False,
        })
        self.assertEqual(response.status_code, 302)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, 'Rua das Flores Atualizada')
        self.assertEqual(self.address.number, '200')

    def test_update_address_of_other_user_returns_404(self):
        other_address = Address.objects.create(
            user=self.other_user,
            street='Rua Secreta',
            number='1',
            neighborhood='Bairro',
            city='Rio de Janeiro',
            state='RJ',
            zip_code='20000-000',
        )
        response = self.client.post(f'/accounts/addresses/update/{other_address.pk}/', {
            'street': 'Invadida',
            'number': '1',
            'complement': '',
            'neighborhood': 'Bairro',
            'city': 'Rio de Janeiro',
            'state': 'RJ',
            'zip_code': '20000-000',
            'is_default': False,
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_address(self):
        response = self.client.post(f'/accounts/addresses/delete/{self.address.pk}/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Address.objects.filter(pk=self.address.pk).exists())

    def test_delete_address_of_other_user_returns_404(self):
        other_address = Address.objects.create(
            user=self.other_user,
            street='Rua Secreta',
            number='1',
            neighborhood='Bairro',
            city='Rio de Janeiro',
            state='RJ',
            zip_code='20000-000',
        )
        response = self.client.post(f'/accounts/addresses/delete/{other_address.pk}/')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Address.objects.filter(pk=other_address.pk).exists())

    def test_set_default_address(self):
        address2 = Address.objects.create(
            user=self.user,
            street='Av. Paulista',
            number='1000',
            neighborhood='Bela Vista',
            city='São Paulo',
            state='SP',
            zip_code='01310-100',
            is_default=True,
        )
        response = self.client.post(f'/accounts/addresses/set-default/{self.address.pk}/')
        self.assertEqual(response.status_code, 302)
        self.address.refresh_from_db()
        address2.refresh_from_db()
        self.assertTrue(self.address.is_default)
        self.assertFalse(address2.is_default)

    def test_set_default_of_other_user_address_returns_404(self):
        other_address = Address.objects.create(
            user=self.other_user,
            street='Rua Secreta',
            number='1',
            neighborhood='Bairro',
            city='Rio de Janeiro',
            state='RJ',
            zip_code='20000-000',
        )
        response = self.client.post(f'/accounts/addresses/set-default/{other_address.pk}/')
        self.assertEqual(response.status_code, 404)
