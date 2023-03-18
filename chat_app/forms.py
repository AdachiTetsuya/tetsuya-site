from django.contrib.sites.shortcuts import get_current_site

from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_username
from dj_rest_auth.forms import AllAuthPasswordResetForm

from .models import AuthCode
from .utils import auth_code_generator


class CustomAllAuthPasswordResetForm(AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]

        for user in self.users:
            # 認証コードを作成して、メールアドレスとともにDBに保存する処理
            auth_code = auth_code_generator()
            AuthCode.objects.create(email=email, auth_code=auth_code)

            context = {
                "current_site": current_site,
                "user": user,
                "request": request,
                "auth_code": auth_code,
            }
            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context["username"] = user_username(user)
            get_adapter(request).send_mail("account/email/password_reset_key", email, context)

        return self.cleaned_data["email"]
