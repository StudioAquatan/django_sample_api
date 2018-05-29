import os
from rest_framework import serializers

from .models import Sound


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['pk', 'name', 'file', 'created_at']

    def validate_file(self, file):
        fname = os.path.basename(file.name)
        _, ext = os.path.splitext(fname)
        if ext[1:] not in ['mp3', 'wav', 'm4a']:
            raise serializers.ValidationError('"{ext}" is not a sound file.'.format(ext=ext))
        return file
