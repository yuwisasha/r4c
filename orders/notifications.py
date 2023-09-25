from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from customers.models import Customer


def send_notification(customer: Customer, model: str, version: str) -> None:
    template = render_to_string(
        "notifications/robot_available.html",
        {"model": model, "version": version}
    )

    send_mail(
        "Заказ",
        message="Робот которым вы инетерсовались уже доступен",
        html_message=template,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[customer.email],
        fail_silently=False,
    )
