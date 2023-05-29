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
        
    def create(self, validated_data):
        conversation_data = validated_data.pop('conversation')
        conversation = ConversationSerializer.create(ConversationSerializer(), validated_data=conversation_data)
        return Message.objects.create(conversation=conversation, **validated_data)