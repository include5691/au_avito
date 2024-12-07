import logging
import requests
from requests.exceptions import RequestException
from .._base import Base

class Chats(Base):

    def get_chats(self, count: int = 100) -> list[dict] | None:
        """Get a list of chats for the authenticated user"""
        user_id = self.get_user_id()
        if user_id is None:
            return None
        url = f'https://api.avito.ru/messenger/v2/accounts/{user_id}/chats'
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }
        result = []
        while len(result) < count:
            try:
                response = requests.get(url, params={"offset": len(result)}, headers=headers)
                data = response.json()
                if not data:
                    return None
                chats = data.get("chats")
                if not chats:
                    break
                result += data.get("chats")
            except RequestException as e:
                logging.error(f"RequestException: Error obtaining chats: {e}")
                break
        return result if result else None