from django.test import TestCase
from catalog.models import Category, Product


class ProductCurrentPriceTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Bolos')
        self.product = Product.objects.create(
            category=self.category,
            name='Bolo de Chocolate',
            price=50.00,
        )

    def test_current_price_returns_price_when_no_promotion(self):
        self.assertEqual(self.product.current_price, 50.00)

    def test_current_price_returns_promotion_price_when_is_promotion_true(self):
        self.product.is_promotion = True
        self.product.promotion_price = 40.00
        self.product.save()
        self.assertEqual(self.product.current_price, 40.00)

    def test_current_price_returns_price_when_is_promotion_but_no_promotion_price(self):
        self.product.is_promotion = True
        self.product.promotion_price = None
        self.product.save()
        self.assertEqual(self.product.current_price, 50.00)
