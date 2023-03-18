from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.utils import email_address_exists
from dj_rest_auth.serializers import PasswordResetConfirmSerializer, PasswordResetSerializer

from chat_app.models import User

from .forms import CustomAllAuthPasswordResetForm


class EmailRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."),
                )
        return email

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
        }

    def save(self, request):
        self.cleaned_data = self.get_cleaned_data()
        email = self.cleaned_data["email"]

        get_adapter().send_confirmation_mail(request, email, signup=True)


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomAllAuthPasswordResetForm


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    uid = serializers.CharField(required=False)
    token = serializers.CharField(required=False)

    def validate(self, attrs):
        self.user = self.context["request"].user
        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user,
            data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        return self.set_password_form.save()


class UserCreateListSerializer(serializers.ListSerializer):
    """User の bulk_create を実現する"""

    def create(self, validated_data):
        instance_list = [User(**attrs) for attrs in validated_data]
        result = User.objects.bulk_create(instance_list)
        return result


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "organization",
            "class_name",
            "username",
            "last_name",
            "first_name",
            "email",
            "is_student",
        ]
        list_serializer_class = UserCreateListSerializer
