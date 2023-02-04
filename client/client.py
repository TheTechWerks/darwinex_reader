import os
import logging
import requests

from dotenv import load_dotenv
from requests import RequestException

from client.models import ProductItem

logger = logging.Logger(__name__)

load_dotenv()


class DarwinClient:
    """
    darwin_client used to connect to the Darwinex Info API
    to fetch all the required details.
    """

    def __init__(self):
        access_token = os.getenv('BEARER_TOKEN')
        self.base_url = os.getenv('API_BASE_URL')
        self.headers = {'Authorization': f'Bearer {access_token}'}

    def get_products_list(self):
        try:
            response = requests.get(f'{self.base_url}products/', headers=self.headers).json()
            products = [dict(ProductItem(**response)) for response in response['content']]
            return products
        except RequestException as e:
            logger.error(f'Failed to get darwin product list: {e}')

