import os

from django.db import models  # noqa: F401,F403


class VideoFile(models.Model):
    def video_upload_path(instance, filename):
        basename = os.path.basename(filename)
        return f"video/{instance.id}/{basename}"

    video = models.FileField("素材動画", upload_to=video_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
