from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self) -> None:
        from orders.signals import robot_available_handler  # noqa