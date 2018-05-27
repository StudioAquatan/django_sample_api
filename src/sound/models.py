import os
import uuid
from django.db import models
from django.utils.safestring import mark_safe


def get_sound_path(instance, filename):
    prefix = 'sounds/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension


class Sound(models.Model):
    name = models.CharField('Sound name', max_length=255)
    file = models.FileField('Sound', upload_to=get_sound_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def sound_tag(self):
        return mark_safe('<audio src="{file}" controls></audio>'.format(file=self.file.url))
