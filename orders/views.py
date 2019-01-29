from rest_framework import generics

from orders.models import Order, OrderDetail
from orders.serializers import OrderSerializer, OrderDetailSerializer


class OrderListView(generics.ListCreateAPIView):
    """
        View to list all orders or create one.

        * for now, no authentication is required
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailListView(generics.ListAPIView):
    """
        View to list a specific order details.

        * for now, no authentication is required
    """
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return OrderDetail.objects.filter(order=self.kwargs.get('pk'))
