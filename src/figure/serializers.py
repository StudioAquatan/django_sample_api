from rest_framework import serializers
from .models import Image


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['pk', 'name', 'file', 'created_at']
