import threading
import requests
import time

from typing import List, Type, Callable

class Message:
    def __init__(self, content: str, chat_id: str, author_username: str = None, author_name: str = None, author_id: str = None):
        self._content = content
        self._chat_id = chat_id
        self._author_username = author_username
        self._author_name = author_name
        self._author_id = author_id

    def reply(self, content: str):
        return Message(content, self._chat_id)
    
    def content(self) -> str:
        return self._content
    
    def author_name(self) -> str:
        return self._author_name
    
    def author_username(self) -> str:
        return self._author_username
    
    def author_id(self) -> str:
        return self._author_id
    
class Command:
    def __init__(self, name: str, description: str, callback: str):
        self._name = name
        self._description = description
        self._callback = callback

class TelegramAPI:
    def __init__(self, token: str):
        self.token = token
        self._update_id = None
        self._message_handler = None

    def send_message(self, message: Message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {"chat_id": message._chat_id, "text": message._content}

        response = requests.post(url, json=payload)
        response.raise_for_status()

    def set_webhook(self, webhook: str):
        url = f"https://api.telegram.org/bot{self.token}/setWebhook"

        payload = {"url": webhook}
        response = requests.post(url, json=payload)

        response.raise_for_status()

    def set_commands(self, commands: List[Command]):
        url = f"https://api.telegram.org/bot{self.token}/setMyCommands"

        command_list = []
        for command in commands:
            command_dict = {
                "command": command._name,
                "description": command._description,
                "callback": command._callback
            }
            command_list.append(command_dict)

        payload = {"commands": command_list}
        response = requests.post(url, json=payload)
        response.raise_for_status()

    def set_message_handler(self, handler):
        self._message_handler = handler

    def _get_updates(self) -> List[Message]:
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        if self._update_id is not None:
            url += f"?offset={self._update_id+1}"
        
        response = requests.get(url)
        response.raise_for_status()

        json = response.json()
        messages = []
        for result in json["result"]:
            try:
                self._update_id = result["update_id"]
                chat_id = result["message"]["chat"]["id"]
                text = result["message"]["text"]
                author = result["message"]["from"]
                author_id = author["id"]
                author_name = author["first_name"]
                author_username = author["username"]
            except KeyError:
                continue

            messages.append(Message(text, chat_id, author_username, author_name, author_id))

        return messages

    def run(self, read_cooldown: int = 1):
        while True:
            try:
                result = self._get_updates()

                threads = []
                for message in result:
                    if self._message_handler is not None:
                        thread = threading.Thread(target=self._message_handler, args=(self, message))
                    thread.start()
                
                    threads.append(thread)
                
            except Exception as e:
                print(f"error: {e}")
            finally:
                time.sleep(read_cooldown)

def message_handler(api: TelegramAPI):
    def wrapper(func: Callable[[TelegramAPI, Message], None]):
        api.set_message_handler(func)
    return wrapper               
