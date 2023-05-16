from rest_framework.serializers import ModelSerializer

from .models import Lodgement_Review

class Lodgement_ReviewSerializer(ModelSerializer):    
    class Meta:
        model = Lodgement_Review
        fields = "__all__"