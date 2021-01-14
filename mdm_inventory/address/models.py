from django.db import models
from django.utils.translation import gettext_lazy as _

class Address(models.Model):
    country = models.CharField(_("País"), max_length=50)
    state = models.CharField(_("Estado"), max_length=50)
    street = models.CharField(_("Calle"), max_length=50)
    municipality =  models.CharField(_("Municipio"), max_length=50)

    def __str__(self):
        return f'{self.country} - {self.state}'
    