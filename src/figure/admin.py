from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created_at'
    )

    readonly_fields = (
        'img_tag',
    )


admin.site.register(Image, ImageAdmin)
