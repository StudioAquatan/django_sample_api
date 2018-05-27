from rest_framework import serializers

from .models import Sound


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['pk', 'name', 'file', 'created_at']
