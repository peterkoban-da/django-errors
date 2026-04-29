"""
Models for Bike App
"""

from django.db.models import Model, CharField


class Bike(Model):
    """
    Model for Bikes
    """

    name: CharField = CharField(max_length=250)
    brand: CharField = CharField(max_length=250)
    color: CharField = CharField(max_length=250)
