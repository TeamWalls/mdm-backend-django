"""Product Model """

from django.db import models
from mdm_inventory.utils.models import BasicModel
from django.utils.translation import gettext_lazy as _

class Product(BasicModel):
    name = models.CharField(_("Nombre"), max_length=50)
    description = models.TextField(_("Descripción") , max_length=180)
    code  = models.CharField(_("Codigo"), max_length=50 , unique=True)
    brand = models.CharField(_("Marca"), max_length=50)
    product_type = models.CharField(_("Tipo Producto"), max_length=50)
    gross_price = models.FloatField(_("Precio Bruto"))
    price_neto = models.FloatField(_("Precio Neto"))

    def __str__(self):
        return f'{self.name} - {self.code}'