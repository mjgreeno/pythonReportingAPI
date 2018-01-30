from rest_framework import serializers
from .models import FarmData


class FarmDataSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = FarmData
        fields = ('message_id', 'dlc', 'payload', 'puc_id', 'ts', 'gps_id', 'latitude', 'longitude', 'groundspeed', 'truecourse')

