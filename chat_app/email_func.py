from django.core.mail import EmailMultiAlternatives


def send_email(subject, text_content, html_content, from_email, to_emails):
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_emails])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
