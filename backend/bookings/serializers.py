from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Booking


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date")

        # assuming lodgement is in data
        if not data['lodgement'].is_available(data['start_date'], data['end_date']):
            raise serializers.ValidationError("The lodgement is not available during this period")

        return data