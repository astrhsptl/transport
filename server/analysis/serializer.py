from rest_framework import serializers

from .models import GivedTransport, Alert, GivedTransportInfo

class GivedTransportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = GivedTransport

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Alert

class GivedTransportInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = GivedTransportInfo