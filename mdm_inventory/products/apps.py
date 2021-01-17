from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ProductConfig(AppConfig):
    name = "mdm_inventory.products"
    verbose_name = _("Productes")
