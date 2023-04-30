from rest_framework.views import APIView
from rest_framework.response import Response

from reservation.models import Location_Place, Location_Review_Ratings
from reservation.serializers import Location_PlaceSerializer


class Location_PlaceAPIView(APIView):
    def get(self, *args, **kwargs):
        locations_places = Location_Place.objects.all()
        serializer = Location_PlaceSerializer(locations_places, many=True)
        return Response(serializer.data)
