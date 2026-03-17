from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_active', 'category']
    list_filter = ['is_active', 'category']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline] # Картинки можно добавлять прямо внутри товара