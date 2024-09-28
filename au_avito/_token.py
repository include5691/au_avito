import os
import requests

def get_token() -> str | None:
    """Get access token by client_id and client_secret"""
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv("CLIENT_ID_KEY"),
        'client_secret': os.getenv("CLIENT_SECRET_KEY"),
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