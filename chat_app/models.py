import os

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    username = models.CharField("ユーザーネーム", max_length=20, unique=True)
    email = models.EmailField("メールアドレス", unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.username

class UserFile(models.Model):

    def file_upload_path(instance, filename):
        basename = os.path.basename(filename)
        return f"file/{instance.id}/{basename}"
    name = models.CharField("名前", max_length=30)
    file = models.FileField("ファイル", upload_to=file_upload_path, blank=True, null=True)