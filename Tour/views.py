from rest_framework import viewsets
from Tour.models import Spot
from Tour.serializers import SpotAdminSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotAdminSerializer

