from rest_framework import serializers
from .models import LocationLoggerModel

class LocationLoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationLoggerModel
        fields = '__all__'