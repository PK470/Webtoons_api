"""Serializer for webtoons"""
from rest_framework import serializers

from core.models import Webtoons

class WebtoonsSerializer(serializers.ModelSerializer):
    """Serializer for webtoons"""
    class Meta:
        model = Webtoons
        fields = ['id', 'title', 'description','character']
        read_only_fields = ['id']

        def create(self, validated_data):
            """Create and return a new webtoon"""
            print(1)
            return Webtoons.objects.create(**validated_data)