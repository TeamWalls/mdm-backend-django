"""
    Models abstracts 
"""

from django.db import models


class ModelDate(models.Model):
    """
        Model to record created and modified
    """
    created = models.DateTimeField(
        'Creado el',
        auto_now_add=True,
        help_text="Date time on wich the object was created")

    modified = models.DateTimeField(
        'Modificado el',
        auto_now=True,
        help_text="Date time on wich the object was modified")

    class Meta:
        """ Meta options"""
        abstract = True
        ordering = ['created', 'modified']
        get_latest_by = ['-created', '-modified']


class BasicModel(models.Model):
    """

        Model to record created, and modified , estado de la instancia 
    """
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(
        'Creado el',
        auto_now_add=True,
        help_text="Date time on wich the object was created")
    modified = models.DateTimeField(
        'Modificado el',
        auto_now=True,
        help_text="Date time on wich the object was modified")

    class Meta:
        """Meta options"""
        abstract = True
        ordering = ['created', 'modified']
        get_latest_by = ['-created', '-modified']
