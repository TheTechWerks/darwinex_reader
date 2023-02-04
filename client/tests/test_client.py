from unittest import TestCase
from unittest.mock import patch

from client.client import DarwinClient


class MockResponse:

    @staticmethod
    def json():
        return {
            'content': [
                {
                    'product_name': 'AAC.5.11',
                    'short_name': 'AAC',
                    'status': 'ACTIVE',
                    'migration_date': 0,
                    'validation_date': 1626081887916,
                    'reset_date': 0,
                    'currency': 'USD'
                }
            ]
        }


class TestDarwinexClient(TestCase):

    @patch("darwin_client.client.requests.get")
    def tests_get_get_products_list(self, mock_client_request):
        mock_client_request.return_value = MockResponse()

        expected_response = [
            {
                'product_name': 'AAC.5.11',
                'short_name': 'AAC',
                'status': 'ACTIVE',
                'migration_date': 0,
                'validation_date': 1626081887916,
                'reset_date': 0,
                'currency': 'USD'
            }
        ]

        client = DarwinClient()
        response = client.get_products_list()

        assert response == expected_response
