import requests
from ._token import get_token

def get_user_id() -> int | None:
    """Get the user ID of the authenticated user"""
    url = 'https://api.avito.ru/core/v1/accounts/self'
    headers = {
        'Authorization': f'Bearer {get_token()}'
    }

    try:
        response = requests.get(url, headers=headers)
        user_data = response.json()
        return user_data.get('id')
    except requests.RequestException as e:
        print(f"Error obtaining user ID: {e}")
        return None