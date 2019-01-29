from django.db import models

from customers.models import Customer
from pizzas.models import Pizza


class Order(models.Model):
    # Status 5 is for special cases where the customer was not home or
    # customer not satisfied with product.
    ORDER_STATUSES = (
        (1, 'Received'),
        (2, 'In Process'),
        (3, 'Out For Delivery'),
        (4, 'Delivered'),
        (5, 'Returned')
    )
    number = models.CharField(
        u'Order #',
        max_length=256,
        unique=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
    )
    status = models.PositiveSmallIntegerField(
        choices=ORDER_STATUSES,
        default=1
    )


class OrderDetail(models.Model):
    PIZZA_SIZE = (
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
        (4, 'Extra Large'),
    )
    order = models.ForeignKey(
        Order,
        verbose_name=u'Order #',
        on_delete=models.CASCADE,
        related_name='details'
    )
    pizza = models.ForeignKey(
        Pizza,
        verbose_name=u'Pizza',
        on_delete=models.DO_NOTHING,
    )
    size = models.PositiveSmallIntegerField(
        u'Size',
        choices=PIZZA_SIZE
    )
    quantity = models.PositiveIntegerField(
        u'quantity',
        default=1
    )
    customer_details = models.TextField(
        u'Details',
        blank=True
    )

    class Meta:
        ordering = ('-pk', )
        unique_together = ('order', 'pizza', 'size',)
