from django.contrib import admin
# Register your models here.
from products.models import Order, Product, OrderItem
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'phone', 'status', 'created_at')
    readonly_fields = ('order_id',)  # Prevent editing
    search_fields = ('order_id', 'customer_name', 'phone')

admin.site.register(Product)
admin.site.register(OrderItem)