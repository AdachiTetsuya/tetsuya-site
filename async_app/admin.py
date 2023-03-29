from django.contrib import admin

from .models import VideoFile


@admin.register(VideoFile)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ("id", "video")
    fields = [
        "video",
    ]
