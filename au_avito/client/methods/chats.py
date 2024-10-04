import requests
from .._base import Base

class ChatsMixin(Base):

    def get_chats(self) -> list[dict] | None:
        """Get a list of chats for the authenticated user"""
        user_id = self.get_user_id()
        if user_id is None:
            return None
        url = f'https://api.avito.ru/messenger/v2/accounts/{user_id}/chats'
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
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