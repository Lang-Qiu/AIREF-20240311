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

    def test_dataset_upload_success(self):
        """
        REQ-102: Verify dataset upload/verification happy path
        """
        url = reverse('data-root')
        data = {
            "data_url": "http://example.com/data.zip",
            "data_token": "valid_token_123"
        }
        # Use format='json' to ensure it sends JSON content type
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("status", response.data)
        self.assertEqual(response.data["status"], "verified")
        self.assertIn("preview", response.data)
        self.assertTrue(len(response.data["preview"]["classes"]) > 0)

    def test_dataset_upload_missing_params(self):
        """
        REQ-102: Verify error handling for missing parameters
        """
        url = reverse('data-root')
        data = {
            "data_url": "http://example.com/data.zip"
            # Missing token
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_model_load_success(self):
        """
        REQ-103: Verify model loading happy path
        """
        url = reverse('model-root')
        data = {
            "model_url": "http://example.com/resnet18.pth",
            "model_type": "pytorch"
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("structure", response.data)
        self.assertEqual(response.data["structure"], "ResNet18")
        self.assertIn("layers", response.data)

    def test_model_load_missing_params(self):
        """
        REQ-103: Verify model loading missing params
        """
        url = reverse('model-root')
        data = {
            "model_type": "pytorch"
            # Missing model_url
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
