from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from allauth.account.models import EmailAddress
from dj_rest_auth.serializers import JWTSerializer
from dj_rest_auth.utils import jwt_encode

from .adapter import AccountAdapter
from .email_func import send_email
from .models import AuthCode, User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def email_auth_code(request):
    auth_code = request.data.get("auth_code")
    type = request.data.get("type")

    auth_code_instance = get_object_or_404(AuthCode, auth_code=auth_code)
    if type == "signup":
        email_instance = EmailAddress.objects.get(email=auth_code_instance.email)
        adapter = AccountAdapter()
        adapter.confirm_email(request, email_address=email_instance)

        user = email_instance.user
        access_token, refresh_token = jwt_encode(user)
        data = {
            "user": user,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        return JsonResponse(JWTSerializer(data).data)

    return JsonResponse({"result": True})


@api_view(["GET"])
def send_email_func(request):
    send_email("こんにちわ", "text", "", "no-replay@tetusya-site.link", "1019born@gmail.com")

    return JsonResponse({"user_data": True})
