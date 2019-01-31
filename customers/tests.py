from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from customers.models import Customer


class AccountTests(APITestCase):
    CUSTOMER_FIELDS_VALIDATION = '''{
        "first_name": ["This field may not be blank."],
        "address": ["This field may not be blank."],
        "phone": ["This field may not be blank."]
    }'''

    def test_create_customer_success(self):
        """
        Ensure we can create a new customer.
        """
        url = reverse('customers:create-list-customers')
        data = {
            'first_name': 'Test',
            'last_name': 'Customer',
            'phone': '23874',
            'address': 'somewhere',
            'email': 'testacc@mail.com'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().full_name, 'Test Customer')

    def test_create_customer_error(self):
        """
        Ensure we validate the data received.
        """
        url = reverse('customers:create-list-customers')
        data = {
            'first_name': '',
            'last_name': '',
            'phone': '',
            'address': '',
            'email': ''
        }

        response = self.client.post(url, data, format='json')

        self.assertJSONEqual(
            response.content, self.CUSTOMER_FIELDS_VALIDATION)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Customer.objects.count(), 0)
