from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Lodgement_Review
from .serializers import Lodgement_ReviewSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Lodgement_Review.objects.all()
    serializer_class = Lodgement_ReviewSerializer

    def list(self, request, id=None):
        """Get Every Lodgements"""
        serializer_class = Lodgement_ReviewSerializer(self.get_queryset(), many=True)
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
