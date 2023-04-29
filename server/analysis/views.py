
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q

from services.distanting import time_to_bus, cord
from .models import GivedTransport, Alert, GivedTransportInfo
from .serializer import GivedTransportSerializer, AlertSerializer, GivedTransportInfoSerializer

from server.celery import app


class GivedTransportViewSet(ModelViewSet):
    queryset = GivedTransport.objects.all()
    serializer_class = GivedTransportSerializer
    permission_classes = (AllowAny,)

class GivedTransportInfoViewSet(ModelViewSet):
    queryset = GivedTransportInfo.objects.all()
    serializer_class = GivedTransportInfoSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            last_record = GivedTransportInfo.objects.latest('pk')
        except:
            last_record = None

        transport, isCreated = GivedTransport.objects.get_or_create(transport_id=data['transport_id'])
    
        data['transport'] = transport.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid()
        
        new_record  = serializer.save()

        self.analysis(new_record, last_record)

        return Response({}, status=status.HTTP_201_CREATED,)
    
    def analysis(self, new_record, last_record, *args, **kwargs):
        nastuchat = lambda record, message: Alert.objects.create(
            gived_id=record.gived_id,
            transport=record.transport,
            lat=record.lat,
            lon=record.lon,
            speed=record.speed,
            created_at=record.created_at,
            alert_message=message,)
        try:

            if new_record.speed > 65:
                nastuchat(new_record, 'Быстро едет')    
            
            if last_record != None:
                analyz_result = cord(
                    (last_record.lat, last_record.lon), 
                    (new_record.lat, new_record.lon))
                

                if analyz_result < 1 and new_record.speed < 10:
                    nastuchat(new_record, 'Медленно едет')

                if (str(last_record.lon) == str(new_record.lon)) and (str(last_record.lat) == str(new_record.lat)):
                    nastuchat(new_record, 'Стотит на месте')
                
                last_record.delete()

        except Exception as e:
            if last_record != None:
                last_record.delete()

class AlertViewSet(ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            period = self.request.GET.get('period')
            if period is not None:
                serializer = self.get_serializer(
                    self.queryset.filter(
                        transport=GivedTransport.objects.get(transport_id=self.request.GET.get('bus_number')), 
                        created_at__gte=period), 
                    many=True)
            else:
                serializer = self.get_serializer(
                    self.queryset.filter(
                        transport=GivedTransport.objects.get(transport_id=self.request.GET.get('bus_number'))), 
                    many=True)
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response([], status.HTTP_204_NO_CONTENT)