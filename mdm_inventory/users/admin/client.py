from django.contrib import admin

from mdm_inventory.users.models import Client

# ADMIN to ProfileUser
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'dni',
        'phone_number',
    )
    list_filter = ('id','first_name','phone_number',)