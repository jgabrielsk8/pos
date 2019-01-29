from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from customers.serializers import CustomerSerializer
from orders.models import Order, OrderDetail
from pizzas.serializers import PizzaSerializer


class OrderDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = (
            'id',
            'pizza',
            'size',
            'quantity',
            'customer_details'
        )
        read_only_fields = ('order',)

    def validate(self, attrs):
        """
        We will override this method to ensure the order details is unique for
        pizza and size
        """
        unique_store = []
        for data in self.initial_data:
            to_validate = (data.get('pizza'), data.get('size'))
            if to_validate in unique_store:
                raise ValidationError({
                    'pizza': ('Already added a pizza with this size, '
                              'consider using quantity')
                })
            unique_store.append(to_validate)
        return super(OrderDetailCreateSerializer, self).validate(attrs)


class OrderDetailRetrieveSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer()

    class Meta:
        model = OrderDetail
        fields = (
            'id',
            'pizza',
            'size',
            'quantity',
            'customer_details'
        )


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id',
            'number',
            'customer',
            'status'
        )

    def get_status(self, obj):
        return obj.get_status_display()


class OrderRetrieveSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    details = OrderDetailRetrieveSerializer(many=True, read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'number',
            'customer',
            'status',
            'details'
        )

    def get_status(self, obj):
        return obj.get_status_display()


class OrderStatusRetrieveSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
        )

    def get_status(self, obj):
        return obj.get_status_display()
