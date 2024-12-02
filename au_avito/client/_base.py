import logging
import requests
from requests.exceptions import RequestException
from cachetools import cached, TTLCache

class Base:

    @cached(cache=TTLCache(maxsize=1, ttl=1))
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
            data = response.json()
            if not data or not isinstance(data, dict):
                return None
            return data.get('access_token')
        except RequestException as e:
            logging.error(f"Error obtaining token: {e} with RequestException")
            return None
        except Exception as e:
            logging.error(f"Error obtaining token: {e}")
            return None
    
    def _get_user_data(self) -> dict | None:
        """Get user data"""
        url = 'https://api.avito.ru/core/v1/accounts/self'
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                logging.error(f"Error obtaining user data: {response.text}")
                return None
            user_data = response.json()
            if not user_data or not isinstance(user_data, dict):
                logging.error(f"Error obtaining user data: {user_data}")
                return None
            return user_data
        except RequestException as e:
            logging.error(f"Error obtaining user data: {e} with RequestException")
            return None
        except Exception as e:
            logging.error(f"Error obtaining token: {e}")
            return None

    def get_user_id(self) -> int | None:
        """Get the user ID of the authenticated user"""
        user_data = self._get_user_data()
        if not user_data:
            return None
        return user_data.get('id')

    def get_user_name(self) -> str | None:
        """Get the name of the authenticated user"""
        user_data = self._get_user_data()
        if not user_data:
            return None
        return user_data.get('name')

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret