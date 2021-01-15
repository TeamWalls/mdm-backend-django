from django.contrib import admin

from mdm_inventory.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'brand'
    )
    list_filter = ('name','brand')
