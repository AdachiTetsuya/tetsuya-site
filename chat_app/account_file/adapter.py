from django.contrib.sites.shortcuts import get_current_site

from allauth.account.adapter import DefaultAccountAdapter

from .utils import auth_code_generator, create_and_save_auth_code, delete_auth_code_from_email


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def send_confirmation_mail(self, request, email, signup):
        current_site = get_current_site(request)

        # 認証コードを作成して、メールアドレスとともにDBに保存する処理
        delete_auth_code_from_email(email)
        auth_code = auth_code_generator()
        create_and_save_auth_code(email=email, auth_code=auth_code)

        ctx = {
            "current_site": current_site,
            "auth_code": auth_code,
        }
        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation"
        self.send_mail(email_template, email, ctx)
