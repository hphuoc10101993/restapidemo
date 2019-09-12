from django.db import models
from django.db.models import ExpressionWrapper, DecimalField, F
from .models import *


class SaleQuerySet(models.QuerySet):
    def calculated_quantity(self):
        return self.model.objects.annotate(
            profit_percentage=ExpressionWrapper(
                (F('profit') / F('revenue')) * 100,
                output_field=DecimalField()
            )
        )


class SaleManager(models.Manager):
    def get_queryset(self):
        return SaleQuerySet(self.model, using=self._db)

    def calculated_quantity(self):
        return self.get_queryset().calculated_quantity()