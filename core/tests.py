from django.test import TestCase
from django.utils import timezone
from catalog.models import Category


class TimeStampedModelTest(TestCase):
    def test_created_at_and_updated_at_auto_filled(self):
        category = Category.objects.create(name='Test Category')
        self.assertIsNotNone(category.created_at)
        self.assertIsNotNone(category.updated_at)
        original_updated_at = category.updated_at
        category.name = 'Updated Category'
        category.save()
        self.assertNotEqual(category.updated_at, original_updated_at)
