from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from manage_user.models import CustomUser

from reservation.models import Lodgement, Lodgement_Review_Ratings
from reservation.serializers import (
    LodgementSerializer,
    LodgementReviewRatingsSerializer,
)


class LodgementViewSet(viewsets.ModelViewSet):
    queryset = Lodgement.objects.all()
    serializer_class = LodgementSerializer

    # def list(self, request, id=None):
    #     """Get Every Lodgements"""
    #     serializer_class = LodgementSerializer(self.get_queryset(), many=True)
    #     headers = self.get_success_headers(serializer_class.data)
    #     return Response(
    #         serializer_class.data, status=status.HTTP_200_OK, headers=headers
    #     )

    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     """Get Lodgement by id"""
    #     lodgement = get_object_or_404(self.get_queryset(), pk=pk)
    #     serializer = self.get_serializer(lodgement)
    #     return Response(serializer.data)

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
        """Delete Lodgement by id"""
        lodgement = get_object_or_404(self.get_queryset(), pk=pk)
        self.perform_destroy(lodgement)
        return Response(status=status.HTTP_204_NO_CONTENT)


class Lodgement_Review_RatingsViewSet(viewsets.ModelViewSet):
    queryset = Lodgement_Review_Ratings.objects.all()
    serializer_class = LodgementReviewRatingsSerializer

    def create(self, request, *args, **kwargs):
        """Create new Lodgement_Review_Rating"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Get Lodgement_Review_Rating by id"""
        lodgement_review_rating = self.get_object()
        serializer = self.get_serializer(lodgement_review_rating)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        """Update Lodgement_Review_Rating by id"""
        lodgement_review_rating = self.get_object()
        serializer = self.get_serializer(
            lodgement_review_rating,
            data=request.data,
            partial=kwargs.pop("partial", False),
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        """Delete Lodgement_Review_Rating by id"""
        lodgement_review_rating = self.get_object()
        self.perform_destroy(lodgement_review_rating)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def list(self, request, id=None):
    #     """Get Every Lodgement_Review_Ratings"""
    #     print(request.data)

    #     serializer_class = LodgementReviewRatingsSerializer(
    #         self.get_queryset(), many=True
    #     )
    #     headers = self.get_success_headers(serializer_class.data)
    #     return Response(
    #         serializer_class.data, status=status.HTTP_200_OK, headers=headers
    #     )

    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     """Get Lodgement_Review_Ratings by id"""
    #     print(request.data)
    #     lodgement_review_rating = get_object_or_404(self.get_queryset(), pk=pk)
    #     serializer = self.get_serializer(lodgement_review_rating)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     """Create new Lodgement_Review_Ratings with user as user_id"""
    #     data_copy = request.data.copy()
    #     assigned_user = CustomUser.objects.get(id=request.user.id)
    #     data_copy["user_id"] = assigned_user.id
    #     serializer = LodgementReviewRatingsSerializer(data=data_copy)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(
    #         serializer.data, status=status.HTTP_201_CREATED, headers=headers
    #     )

    # def update(self, request, pk=None, *args, **kwargs):
    #     """Update Lodgement_Review_Ratings by id"""

    #     data_copy = request.data.copy()
    #     assigned_user = CustomUser.objects.get(id=request.user.id)
    #     data_copy["user_id"] = assigned_user.id

    #     queryset = Lodgement_Review_Ratings.objects.filter(pk=pk)
    #     lodgement_review_rating = get_object_or_404(queryset, pk=pk)
    #     serializer = LodgementReviewRatingsSerializer(
    #         lodgement_review_rating, data=data_copy
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    # def destroy(self, request, pk=None, *args, **kwargs):
    #     """Delete Lodgement_Review_Ratings by id"""
    #     lodgement_review_rating = get_object_or_404(self.get_queryset(), pk=pk)
    #     self.perform_destroy(lodgement_review_rating)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
