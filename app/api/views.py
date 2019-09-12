from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.api.filter import SalesFilter
from app.api.serializers import SaleSerializer
from app.models import Sales


class SaleListApiView(ListAPIView):
    serializer_class = SaleSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    queryset = Sales.objects.calculated_quantity()
    filter_class = SalesFilter
    fields = ('id', 'region', 'country', 'ptype', 'channel', 'date', 'quantity',
              'price', 'cost', 'revenue', 'profit', 'profit_percentage')
    filter_fields = fields
    search_fields = fields

