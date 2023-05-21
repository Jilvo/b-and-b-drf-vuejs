from rest_framework.serializers import ModelSerializer

from .models import Conversation, Message


class ConversationSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    conversation = ConversationSerializer()
    class Meta:
        model = Message
        fields = "__all__"
