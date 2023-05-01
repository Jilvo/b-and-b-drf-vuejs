from rest_framework.serializers import ModelSerializer

from reservation.models import Lodgement, Lodgement_Review_Ratings


class LodgementSerializer(ModelSerializer):
    class Meta:
        model = Lodgement
        fields = "__all__"
class LodgementReviewRatingsSerializer(ModelSerializer):
    class Meta:
        model = Lodgement
        fields = "__all__"
