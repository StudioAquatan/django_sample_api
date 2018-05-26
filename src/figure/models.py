import os
import uuid
from django.db import models
from django.utils.safestring import mark_safe


def get_image_path(instance, filename):
    prefix = 'images/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension


class Image(models.Model):
    name = models.CharField('Image title', max_length=255)
    file = models.ImageField('Image', upload_to=get_image_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def img_tag(self):
        return mark_safe('<img src="{url}" style="max-width: 520px;height: auto;">'.format(url=self.file.url))

    def __str__(self):
        return self.name
