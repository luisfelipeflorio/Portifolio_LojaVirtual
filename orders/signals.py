from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order


@receiver(post_save, sender=Order)
def send_order_confirmation(sender, instance, created, **kwargs):
    if created:
        context = {
            'order': instance,
            'items': instance.items.all(),
        }
        
        html_content = render_to_string('orders/email/order_confirmation.html', context)
        text_content = render_to_string('orders/email/order_confirmation.txt', context)
        
        send_mail(
            subject=f'Pedido {instance.protocol} - Confirmação',
            message=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.customer_email],
            html_message=html_content,
            fail_silently=False,
        )