import random
from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Order(TimeStampedModel):
    STATUS_RECEIVED = 'received'
    STATUS_PREPARING = 'preparing'
    STATUS_READY = 'ready'
    STATUS_DELIVERED = 'delivered'

    STATUS_CHOICES = [
        (STATUS_RECEIVED, 'Recebido'),
        (STATUS_PREPARING, 'Em preparo'),
        (STATUS_READY, 'Pronto'),
        (STATUS_DELIVERED, 'Entregue'),
    ]

    DELIVERY_PICKUP = 'pickup'
    DELIVERY_DELIVERY = 'delivery'

    DELIVERY_CHOICES = [
        (DELIVERY_PICKUP, 'Retirada na loja'),
        (DELIVERY_DELIVERY, 'Entrega'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='cliente'
    )
    protocol = models.CharField('protocolo', max_length=20, unique=True)
    status = models.CharField(
        'status',
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_RECEIVED
    )
    delivery_type = models.CharField(
        'tipo de entrega',
        max_length=20,
        choices=DELIVERY_CHOICES,
        default=DELIVERY_PICKUP
    )
    customer_name = models.CharField('nome do cliente', max_length=200)
    customer_email = models.EmailField('e-mail do cliente')
    customer_phone = models.CharField('telefone do cliente', max_length=20)
    delivery_address = models.TextField('endereço de entrega', blank=True)
    scheduled_at = models.DateTimeField('data/hora agendada', null=True, blank=True)
    notes = models.TextField('observações', blank=True)
    subtotal = models.DecimalField('subtotal', max_digits=10, decimal_places=2, default=0)
    delivery_fee = models.DecimalField('frete', max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField('total', max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.protocol:
            self.protocol = self.generate_protocol()
        super().save(*args, **kwargs)

    def generate_protocol(self):
        year = models.DateField().today().year
        random_part = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        return f'CON-{year}{random_part}'

    def __str__(self):
        return self.protocol

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['-created_at']


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='pedido'
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='produto'
    )
    product_name = models.CharField('nome do produto', max_length=200)
    unit_price = models.DecimalField('preço unitário', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('quantidade', default=1)
    subtotal = models.DecimalField('subtotal', max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product_name} x {self.quantity}'

    class Meta:
        verbose_name = 'item do pedido'
        verbose_name_plural = 'itens do pedido'