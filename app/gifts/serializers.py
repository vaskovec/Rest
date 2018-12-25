from rest_framework import serializers
from .models import (
    Gift,
    GiftRequest,
    GiftApprove,
)


class GiftSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gift
        fields = '__all__'


class GiftRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GiftRequest
        fields = '__all__'


class GiftApproveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GiftApprove
        fields = '__all__'