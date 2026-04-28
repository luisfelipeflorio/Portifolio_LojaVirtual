from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'unit_price', 'quantity', 'subtotal']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['protocol', 'customer_name', 'status', 'total', 'created_at']
    list_filter = ['status', 'delivery_type', 'created_at']
    search_fields = ['protocol', 'customer_name', 'customer_email']
    readonly_fields = ['protocol', 'user', 'created_at', 'updated_at']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_name', 'unit_price', 'quantity', 'subtotal']
    search_fields = ['product_name', 'order__protocol']