from rest_framework import serializers
from django.db import IntegrityError
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'owner',
            'post',
            'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
