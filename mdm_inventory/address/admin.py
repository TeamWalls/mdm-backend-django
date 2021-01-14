from django.contrib import admin

from mdm_inventory.address.models import Address

# ADMIN to ProfileUser
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'country',
        'state',
        'municipality',
        'street',
    )
    list_filter = ('id','country','state','municipality','street')