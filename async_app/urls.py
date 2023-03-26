from django.urls import path

from . import views

app_name = "async_app"

urlpatterns = [
    path("celery-test/", views.celery_test, name="celery_test"),
]
