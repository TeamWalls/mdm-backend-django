from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AddressConfig(AppConfig):
    name = "mdm_inventory.address"
    verbose_name = _("Address")
