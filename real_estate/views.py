from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .models import Property
from .serializers import PropertySerializer

# Create your views here.
class PropertyViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = Property.objects.select_related("address").all()
    serializer_class = PropertySerializer
