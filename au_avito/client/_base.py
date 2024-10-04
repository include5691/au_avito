import os
import requests
from cachetools import cached, TTLCache

class Base:

    @cached(cache=TTLCache(maxsize=1, ttl=10))
    def get_token(self) -> str | None:
        """Get access token by client_id and client_secret"""
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        url = 'https://api.avito.ru/token/'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            response = requests.post(url, data=data, headers=headers, timeout=10)
            token_data = response.json()
            return token_data['access_token']
        except requests.RequestException as e:
            print(f"Error obtaining token: {e}")
            return None

    def get_user_id(self) -> int | None:
        """Get the user ID of the authenticated user"""
        url = 'https://api.avito.ru/core/v1/accounts/self'
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }

        try:
            response = requests.get(url, headers=headers)
            user_data = response.json()
            return user_data.get('id')
        except requests.RequestException as e:
            print(f"Error obtaining user ID: {e}")
            return None

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret