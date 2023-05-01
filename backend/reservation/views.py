from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from reservation.models import Lodgement, Lodgement_Review_Ratings
from reservation.serializers import (
    LodgementSerializer,
    LodgementReviewRatingsSerializer,
)


class LodgementViewSet(viewsets.ModelViewSet):
    locations_places = Lodgement.objects.all()
    serializer = LodgementSerializer(locations_places, many=True)

    def get(self, *args, **kwargs):
        locations_places = Lodgement.objects.all()
        serializer = LodgementSerializer(locations_places, many=True)
        return Response(serializer.data)


class Lodgement_Review_RatingsViewSet(viewsets.ModelViewSet):
    lodgement_review_ratings = Lodgement_Review_Ratings.objects.all()
    serializer = LodgementReviewRatingsSerializer(lodgement_review_ratings, many=True)

    def get(self, *args, **kwargs):
        lodgement_review_ratings = Lodgement_Review_Ratings.objects.all()
        serializer = LodgementReviewRatingsSerializer(
            lodgement_review_ratings, many=True
        )
        return Response(serializer.data)
