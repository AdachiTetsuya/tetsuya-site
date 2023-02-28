from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    User
)
from .serializers import (
    UserSerializer
)
from django.http import JsonResponse
from .email_func import send_email
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    


@api_view(["GET"])
def send_email_func(request):
    send_email("こんにちわ", "text", "", "no-replay@tetusya-site.link", "1019born@gmail.com")

    return JsonResponse({"user_data": True})