from django.urls import include, path
from rest_framework import routers

from . import views
from .account_file.views import email_auth_code, post_register_email

app_name = "chat_app"

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("post-register-email/", post_register_email, name="post_register_email"),
    path("email-auth-code/", email_auth_code, name="email_auth_code"),
]
