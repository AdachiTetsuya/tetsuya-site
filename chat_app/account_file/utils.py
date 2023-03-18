import random
import string

from chat_app.models import AuthCode


def auth_code_generator(size=6, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def delete_auth_code_from_email(email):
    instances = AuthCode.objects.filter(email=email)
    for instance in instances:
        instance.delete()


def create_and_save_auth_code(email, auth_code):
    AuthCode.objects.create(email=email, auth_code=auth_code)
