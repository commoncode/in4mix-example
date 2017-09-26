from rest_framework import serializers


from . import models


class SparePartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SparePart
        fields = ('id', 'master_product', 'spare')
