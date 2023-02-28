from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "chat_app"

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("send-email/", views.send_email_func, name="send_email_func")
]
