from rest_framework import serializers

from dj_rest_auth.serializers import PasswordResetSerializer

from .forms import CustomAllAuthPasswordResetForm
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomAllAuthPasswordResetForm
