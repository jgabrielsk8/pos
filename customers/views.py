from rest_framework import viewsets

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerListView(viewsets.ModelViewSet):
    """
        View to list all customers or create one.

        * for now, no authentication is required
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
