from django.conf.urls import url, include
from .models import *
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ("id","name", "lat", "lng")

class ObsSerializer(serializers.ModelSerializer):
    # unit = serializers.ReadOnlyField(source='Unit', read_only=True)

    class Meta:
        model = Observation
        fields = ("id",'unit', 'timestamp', 'intensity')

class ObsViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObsSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    @detail_route(methods=['get'])
    def all_obs_for_unit(self, request, pk=None):
        unit = Unit.objects.get(id = pk)
        queryset = Observation.objects.filter(unit=unit)
        serializer = ObsSerializer(queryset, many=True)
        return Response(serializer.data)
