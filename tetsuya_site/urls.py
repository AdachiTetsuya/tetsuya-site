from django.contrib import admin
from django.urls import include, path

from chat_app.account_file.views import (
    CustomPasswordResetConfirmView,
    CustomRegisterView,
    CustomResendEmailVerificationView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "dj-rest-auth/registration/resend-email/",
        CustomResendEmailVerificationView.as_view(),
        name="resend_email",
    ),
    path(
        "dj-rest-auth/registration/",
        CustomRegisterView.as_view(),
        name="registration",
    ),
    path(
        "password/reset/confirm/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("chat-app/", include("chat_app.urls")),
]
