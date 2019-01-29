from rest_framework import generics

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerListView(generics.ListCreateAPIView):
    """
        View to list all customers or create one.

        * for now, no authentication is required
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
