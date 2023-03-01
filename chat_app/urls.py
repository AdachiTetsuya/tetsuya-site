from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "chat_app"

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("email-auth-code/", views.email_auth_code, name="email_auth_code"),
    path("send-email/", views.send_email_func, name="send_email_func"),
]
