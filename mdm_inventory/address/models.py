from django.db import models
from django.utils.translation import gettext_lazy as _
from mdm_inventory.utils.models import BasicModel

class Address(BasicModel):
    client = models.ForeignKey("clients.Client", verbose_name=_("Client_Address"), on_delete=models.CASCADE)
    country = models.CharField(_("País"), max_length=50)
    state = models.CharField(_("Estado"), max_length=50)
    street = models.CharField(_("Calle"), max_length=50)
    municipality =  models.CharField(_("Municipio"), max_length=50)

    def __str__(self):
        return f'{self.country} - {self.state}'
    