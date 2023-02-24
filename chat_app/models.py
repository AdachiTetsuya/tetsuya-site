from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    username = models.CharField("ユーザーネーム", max_length=20, unique=False)
    email = models.EmailField("メールアドレス", unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.username
