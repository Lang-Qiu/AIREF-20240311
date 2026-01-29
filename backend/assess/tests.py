from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class BaseRoutesTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_data_route_exists(self):
        # We expect these names to be defined
        try:
            url = reverse('data-root')
        except:
            self.fail("URL 'data-root' not found")
        
        response = self.client.post(url)
        # We expect 501 or 405, but definitely NOT 404
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_model_route_exists(self):
        try:
            url = reverse('model-root')
        except:
            self.fail("URL 'model-root' not found")
        
        response = self.client.post(url)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_attack_route_exists(self):
        try:
            url = reverse('attack-root')
        except:
            self.fail("URL 'attack-root' not found")
        
        response = self.client.post(url)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
