import re
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q

from .models import Town, Stop, Transport
from .serializers import TownSerializer, StopSerializer, TransportSerializer


class TownViewSet(ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            input_query_string = self.request.GET.get('q')
            serializer = self.get_serializer(
                Town.objects.filter(
                    Q(name__icontains=input_query_string.capitalize()) | Q(name__icontains=input_query_string.lower()) | Q(name__icontains=input_query_string) )
                , many=True)
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        except:
            return super().list(request, *args, **kwargs)

class StopViewSet(ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(
                self.queryset.filter(
                    town_id=Town.objects.get(id=self.request.GET.get('town_id'))), 
                many=True)
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        except:
            return super().list(request, *args, **kwargs)


class TransportViewSet(ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            bus_number = self.request.GET.get('bus_number')
            if bus_number and not bus_number.isalpha():
                serializer = self.get_serializer(
                    self.queryset.filter(
                    number=self.request.GET.get('bus_number'),
                    town_id=Town.objects.get(id=self.request.GET.get('town_id'))), 
                many=True)
            else:
                serializer = self.get_serializer(
                    self.queryset.filter(
                    Q(town_id=Town.objects.get(id=self.request.GET.get('town_id')))), 
                many=True)
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        except: 
            return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)