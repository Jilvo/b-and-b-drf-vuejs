from django.shortcuts import render, get_object_or_404
from manage_user.models import CustomUser
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request, id=None):
        """Get Every Lodgements"""
        serializer_class = BookingSerializer(self.get_queryset(), many=True)
        headers = self.get_success_headers(serializer_class.data)
        return Response(
            serializer_class.data, status=status.HTTP_200_OK, headers=headers
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Get Lodgement by id"""
        conversation = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(conversation)
        response_data = serializer.data
        return Response({"conversation": response_data})
    
    def create(self, request, *args, **kwargs):
        """ Create a new Booking"""
        data_copy = request.data.copy()
        assigned_user = CustomUser.objects.get(id=request.user.id)
        data_copy["user_id"] = assigned_user.id        
        serializer = BookingSerializer(data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, pk=None, *args, **kwargs):
        """Update Booking"""
        data_copy = request.data.copy()
        serializer = BookingSerializer(data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        """Delete Conversation (by id) """
        conversation = get_object_or_404(self.get_queryset(), pk=pk)
        self.perform_destroy(conversation)
        return Response(status=status.HTTP_204_NO_CONTENT)