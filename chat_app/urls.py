from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "chat_app"

router = routers.DefaultRouter()
# router.register("user", views.ClassInfoViewSet, basename="class_info")


urlpatterns = [
    path("", include(router.urls)),
]
