from rest_framework import generics

from pizzas.models import Pizza
from pizzas.serializers import PizzaSerializer


class PizzaListView(generics.ListCreateAPIView):
    """
        View to list all pizzas or create one.

        * for now, no authentication is required
    """
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
