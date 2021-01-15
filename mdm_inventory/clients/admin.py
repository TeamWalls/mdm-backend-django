from django.contrib import admin

from mdm_inventory.clients.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'dni',
        'phone_number',
        'address'
    )
    list_filter = ('phone_number',)
