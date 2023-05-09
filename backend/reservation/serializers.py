from rest_framework.serializers import ModelSerializer

from reservation.models import (
    Lodgement,
    Lodgement_Review_Ratings,
    Bathroom_Lodgement_Equipment,
    Bedroom_Lodgement_Equipment,
    Distraction_Lodgement_Equipment,
    Family_Lodgement_Equipment,
    Climatisation_Lodgement_Equipment,
    Home_Security_Lodgement_Equipment,
    Internet_Lodgement_Equipment,
    Kitchen_Logdment_Equipment,
    Exterior_Lodgement_Equipment,
    Parking_Lodgement_Equipment,
    Services_Lodgement,
)


class LodgementSerializer(ModelSerializer):
    class Meta:
        model = Lodgement
        fields = "__all__"


class LodgementReviewRatingsSerializer(ModelSerializer):
    class Meta:
        model = Lodgement_Review_Ratings
        fields = "__all__"


class BathroomLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Bathroom_Lodgement_Equipment
        fields = "__all__"


class BedroomLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Bedroom_Lodgement_Equipment
        fields = "__all__"


class DistractionLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Distraction_Lodgement_Equipment
        fields = "__all__"


class FamilyLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Family_Lodgement_Equipment
        fields = "__all__"


class ClimatisationLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Climatisation_Lodgement_Equipment
        fields = "__all__"


class HomeSecurityLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Home_Security_Lodgement_Equipment
        fields = "__all__"


class InternetLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Internet_Lodgement_Equipment
        fields = "__all__"


class KitchenLogdmentEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Kitchen_Logdment_Equipment
        fields = "__all__"


class ExteriorLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Exterior_Lodgement_Equipment
        fields = "__all__"


class ParkingLodgementEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Parking_Lodgement_Equipment
        fields = "__all__"


class ServicesLodgementSerializer(ModelSerializer):
    class Meta:
        model = Services_Lodgement
        fields = "__all__"
