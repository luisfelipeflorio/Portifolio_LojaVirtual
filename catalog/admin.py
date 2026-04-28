from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'sort_order', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'current_price', 'is_active', 'is_featured', 'is_promotion', 'stock', 'created_at']
    list_filter = ['category', 'is_active', 'is_featured', 'is_promotion']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}

    def current_price(self, obj):
        return obj.current_price
    current_price.short_description = 'Preço Atual'
