from django.db.models.signals import pre_save
from django.dispatch import receiver

from robots.models import Robot
from customers.models import Customer
from orders.models import Order
from orders.notifications import send_notification


@receiver(pre_save, sender=Robot)
def robot_available_handler(sender, instance: Robot, **kwargs) -> None:
    robot = Robot.objects.filter(serial=instance.serial).first()

    if not robot:
        orders = Order.objects.filter(robot_serial=instance.serial)
        for order in orders:
            customer = Customer.objects.get(id=order.customer_id)
            send_notification(customer, instance.model, instance.version)
            order.delete()
