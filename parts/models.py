from django.db import models


class Product(models.Model):

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)


class SparePart(models.Model):

    master_product = models.ForeignKey('parts.Product', related_name='spare_parts')
    spare = models.ForeignKey('parts.Product', related_name='+')

    class Meta:
        unique_together = (
            ('master_product', 'spare'),
        )
