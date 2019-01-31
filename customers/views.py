from rest_framework import viewsets

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerCreateListView(viewsets.ModelViewSet):
    """
    View to create and list all customers.
    * for now, no authentication is required
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_fields = ('id', 'first_name', 'phone', 'email', )


class CustomerUpdateView(viewsets.ModelViewSet):
    """
    View to update a customers.
    * for now, no authentication is required
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
