from django.urls import include, path
from rest_framework import routers

from .views import VideoFileViewSet, celery_test

app_name = "async_app"

router = routers.DefaultRouter()
router.register("video-file", VideoFileViewSet, basename="video_file")

urlpatterns = [
    path("", include(router.urls)),
    path("celery-test/", celery_test, name="celery_test"),
]
