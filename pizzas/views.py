from rest_framework import generics

from pizzas.models import Pizza
from pizzas.serializers import PizzaSerializer


class PizzaListView(generics.ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
