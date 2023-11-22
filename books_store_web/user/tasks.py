from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_welcome_email(email):
    """Задача для отправки сообщений при регистрации пользователя."""
    # subject = "Welcome to Our Service!"
    # message = "Hello! Thank you for registering with us. We are excited to have you on board."
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail(subject, message, email_from, recipient_list)
    pass
