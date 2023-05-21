from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, id=None):
        """Get Every Conversation"""
        serializer_class = MessageSerializer(self.get_queryset(), many=True)
        headers = self.get_success_headers(serializer_class.data)
        return Response(
            serializer_class.data, status=status.HTTP_200_OK, headers=headers
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Get Conversation by id"""
        conversation = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(conversation)
        response_data = serializer.data
        return Response({"conversation": response_data})

    def create(self, request, pk=None, *args, **kwargs):
        """ Create Conversation"""
        print(request.data)  
        return Response(status=status.HTTP_200_OK)
