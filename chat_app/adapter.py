from allauth.account.adapter import DefaultAccountAdapter

from .models import AuthCode
from .utils import auth_code_generator


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        # 認証コードを作成して、メールアドレスとともにDBに保存する処理
        auth_code = auth_code_generator()
        AuthCode.objects.create(email=email, auth_code=auth_code)

        # メールの本文をカスタマイズする処理
        context.update({"auth_code": auth_code})
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
