from django.shortcuts import render,get_object_or_404
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
