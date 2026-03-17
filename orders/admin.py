from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0 # Чтобы не было пустых строк по умолчанию

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'phone']
    inlines = [OrderItemInline]