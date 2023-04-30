from rest_framework.serializers import ModelSerializer

from reservation.models import Location_Place, Location_Review_Ratings


class Location_PlaceSerializer(ModelSerializer):
    class Meta:
        model = Location_Place
        fields = "__all__"
