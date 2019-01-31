from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pizzas.models import Pizza


class PizzaTests(APITestCase):
    PIZZA_FIELDS_VALIDATION = '''{
        "name":["This field may not be blank."]
    }'''

    def test_create_pizza_success(self):
        """
        Ensure we can create a new pizza.
        """
        url = reverse('pizzas:create-list-pizzas')
        data = {
            'name': 'Pepperoni',
            'description': 'Delicious',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)
        self.assertEqual(Pizza.objects.get().name, 'Pepperoni')

    def test_create_pizza_error(self):
        """
        Ensure we validate the data received.
        """
        url = reverse('pizzas:create-list-pizzas')
        data = {
            'name': '',
            'description': '',
        }

        response = self.client.post(url, data, format='json')

        self.assertJSONEqual(
            response.content, self.PIZZA_FIELDS_VALIDATION)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Pizza.objects.count(), 0)
