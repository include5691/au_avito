import logging
import requests
from requests.exceptions import RequestException
from .._base import Base

class Messages(Base):

    def get_messages(self, chat_id: str) -> dict | None:
        """Get messages by its ID"""
        user_id = self.get_user_id()
        if user_id is None:
            return None
        url = f'https://api.avito.ru/messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/'
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            if not data:
                return None
            if 'messages' in data:
                return data['messages']
        except requests.RequestException as e:
            logging.error(f"RequestException: Error obtaining chat: {e}")
            return None