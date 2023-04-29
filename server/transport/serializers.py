from rest_framework import serializers

from .models import Town, Stop, Transport

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Town

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Stop

class TransportSerializer(serializers.ModelSerializer):
    stops = StopSerializer(many=True)
    town = TownSerializer()
    class Meta:
        fields = ('__all__')
        model = Transport