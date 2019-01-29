from rest_framework import serializers

from orders.models import Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'number',
            'customer',
            'status',
        )


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = (
            'id',
            'customer',
            'pizza',
            'size',
            'quantity',
            'customer_details'
        )
