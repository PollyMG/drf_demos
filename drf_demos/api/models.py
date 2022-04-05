from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    NAME_MAX_LENGTH = 15

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    descriptions = models.TextField(
        null=True,
        blank=True,
    )

class Product(models.Model):
    NAME_MAX_LENGTH = 25
    PRICE_MIN_VALUE = 0.01

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(PRICE_MIN_VALUE))],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )



