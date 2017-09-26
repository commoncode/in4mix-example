from rest_framework import generics

from . import models
from . import serializers


class SparePartListAPIView(generics.ListAPIView):
    """
    Provides an optionally filtered list of spare parts
    """

    queryset = models.SparePart.objects.all()
    serializer_class = serializers.SparePartSerializer

    def filter_queryset(self, queryset):
        if 'product' in self.request.GET:
            queryset = queryset.filter(master_product=self.request.GET['product'])
        return queryset[0:100]
