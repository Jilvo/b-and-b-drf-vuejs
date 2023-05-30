from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from manage_user.models import CustomUser

from .models import (
    Lodgement,
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
from .serializers import (
    BathroomLodgementEquipmentSerializer,
    BedroomLodgementEquipmentSerializer,
    ClimatisationLodgementEquipmentSerializer,
    DistractionLodgementEquipmentSerializer,
    ExteriorLodgementEquipmentSerializer,
    FamilyLodgementEquipmentSerializer,
    HomeSecurityLodgementEquipmentSerializer,
    InternetLodgementEquipmentSerializer,
    KitchenLogdmentEquipmentSerializer,
    LodgementSerializer,
    ParkingLodgementEquipmentSerializer,
    ServicesLodgementSerializer,
)


class LodgementViewSet(viewsets.ModelViewSet):
    queryset = Lodgement.objects.all()
    serializer_class = LodgementSerializer

    def list(self, request, id=None):
        """Get Every Lodgements"""
        serializer_class = LodgementSerializer(self.get_queryset(), many=True)
        headers = self.get_success_headers(serializer_class.data)
        return Response(
            serializer_class.data, status=status.HTTP_200_OK, headers=headers
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Get Lodgement by id"""
        lodgement = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(lodgement)
        response_data = serializer.data
        # Bathroom_Lodgement_Equipment
        response_data["bathroom_equipment"] = BathroomLodgementEquipmentSerializer(
            Bathroom_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Bedroom_Lodgement_Equipment
        response_data["bedroom_equipment"] = BedroomLodgementEquipmentSerializer(
            Bedroom_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Distraction_Lodgement_Equipment
        response_data[
            "distraction_equipment"
        ] = DistractionLodgementEquipmentSerializer(
            Distraction_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Family_Lodgement_Equipment
        response_data["family_equipment"] = FamilyLodgementEquipmentSerializer(
            Family_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Climatisation_Lodgement_Equipment
        response_data[
            "climatisation_equipment"
        ] = ClimatisationLodgementEquipmentSerializer(
            Climatisation_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Home_Security_Lodgement_Equipment
        response_data[
            "home_security_equipment"
        ] = HomeSecurityLodgementEquipmentSerializer(
            Home_Security_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Internet_Lodgement_Equipment
        response_data["internet_equipment"] = InternetLodgementEquipmentSerializer(
            Internet_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Kitchen_Logdment_Equipment
        response_data["kitchen_equipment"] = KitchenLogdmentEquipmentSerializer(
            Kitchen_Logdment_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Exterior_Lodgement_Equipment
        response_data["exterior_equipment"] = ExteriorLodgementEquipmentSerializer(
            Exterior_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Parking_Lodgement_Equipment
        response_data["parking_equipment"] = ParkingLodgementEquipmentSerializer(
            Parking_Lodgement_Equipment.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        # Services_Lodgement
        response_data["services"] = ServicesLodgementSerializer(
            Services_Lodgement.objects.filter(lodgement_id=lodgement),
            many=True,
        ).data

        return Response({"lodgement": response_data})

    def create(self, request, *args, **kwargs):
        """Create new Lodgement with user as user_id"""
        data_copy = request.data.copy()
        assigned_user = CustomUser.objects.get(id=request.user.id)
        data_copy["user_id"] = assigned_user.id
        serializer = LodgementSerializer(data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, pk=None, *args, **kwargs):
        """Update Lodgement by id"""

        data_copy = request.data.copy()
        assigned_user = CustomUser.objects.get(id=request.user.id)
        data_copy["user_id"] = assigned_user.id

        queryset = Lodgement.objects.filter(pk=pk)
        lodgement = get_object_or_404(queryset, pk=pk)
        serializer = LodgementSerializer(lodgement, data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, pk=None, *args, **kwargs):
        """Delete Lodgement (by id) and Equipments if exists"""
        lodgement = get_object_or_404(self.get_queryset(), pk=pk)
        self.perform_destroy(lodgement)
        return Response(status=status.HTTP_204_NO_CONTENT)


