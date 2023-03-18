from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.serializers import ResendEmailVerificationSerializer
from dj_rest_auth.registration.views import ResendEmailVerificationView
from dj_rest_auth.serializers import JWTSerializer
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.views import PasswordResetConfirmView

from chat_app.models import AuthCode

from .serializers import EmailRegisterSerializer
from .utils import delete_auth_code_from_email

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("password1", "password2"),
)


class CustomRegisterView(CreateAPIView):
    serializer_class = api_settings.REGISTER_SERIALIZER
    permission_classes = api_settings.REGISTER_PERMISSION_CLASSES
    token_model = TokenModel
    throttle_scope = "dj_rest_auth"

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_response_data(self, user):
        data = {
            "user": user,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
        }
        return JWTSerializer(data, context=self.get_serializer_context()).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if api_settings.USE_JWT:
            self.access_token, self.refresh_token = jwt_encode(user)
        email_instance = EmailAddress.objects.get(user=user, email=user.email)
        get_adapter().confirm_email(request=self.request, email_address=email_instance)
        return user


@api_view(["POST"])
@permission_classes([AllowAny])
def email_auth_code(request):
    auth_code = request.data.get("auth_code")
    type_data = request.data.get("type")
    email = request.data.get("email")

    auth_code_instance = get_object_or_404(AuthCode, auth_code=auth_code, email=email)

    if type_data == "signUp":
        auth_code_instance.delete()
        return JsonResponse({"type": type_data, "result": True})

    else:
        email_instance = EmailAddress.objects.get(email=auth_code_instance.email)
        auth_code_instance.delete()
        user = email_instance.user
        access_token, refresh_token = jwt_encode(user)
        data = {
            "user": user,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        jwt_auth_data = JWTSerializer(data).data

        return JsonResponse({"type": type_data, "jwt_auth_data": jwt_auth_data})


@api_view(["POST"])
@permission_classes([AllowAny])
def post_register_email(request):
    """サインアップ時にメールアドレスをpostするところ"""
    serializer = EmailRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(request)
    return JsonResponse({"detail": _("Verification e-mail sent.")}, status=status.HTTP_200_OK)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    serializer_class = api_settings.PASSWORD_RESET_SERIALIZER
    permission_classes = (IsAuthenticated,)
    throttle_scope = "dj_rest_auth"

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": _("Password has been reset with the new password.")},
        )


class CustomResendEmailVerificationView(ResendEmailVerificationView):
    permission_classes = (AllowAny,)
    serializer_class = ResendEmailVerificationSerializer
    queryset = EmailAddress.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")

        if email:
            delete_auth_code_from_email(email)

            get_adapter(request).send_confirmation_mail(request, email, signup=False)

        return Response({"detail": _("ok")}, status=status.HTTP_200_OK)
