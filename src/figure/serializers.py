from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Image


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['pk', 'name', 'file', 'created_at']


class Base64ImageSerializer(serializers.ModelSerializer):
    file = Base64ImageField()

    class Meta:
        model = Image
        fields = ['pk', 'name', 'file', 'created_at']
