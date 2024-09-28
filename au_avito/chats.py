import requests
from ._token import get_token
from .user import get_user_id

def get_chats() -> list[dict] | None:
    """Get a list of chats for the authenticated user"""
    user_id = get_user_id()
    if user_id is None:
        return None
    url = f'https://api.avito.ru/messenger/v2/accounts/{user_id}/chats'
    headers = {
        'Authorization': f'Bearer {get_token()}'
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if not data:
            return None
        return data.get("chats")
    except requests.RequestException as e:
        print(f"Error obtaining chats: {e}")
        return None