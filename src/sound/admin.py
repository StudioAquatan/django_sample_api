from django.contrib import admin

from .models import Sound


class SoundAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
    )

    readonly_fields = (
        'sound_tag',
    )


admin.site.register(Sound, SoundAdmin)
