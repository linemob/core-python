from linebot.models import (
    ImagemapSendMessage,
)


class ImagemapMessage():

    def __init__(self, command):
        self.base_url = command.get_message()['base_url']
        self.alt_text = command.get_message()['alt_text']
        self.base_size = command.get_message()['base_size']
        self.actions = command.get_message()['actions']

    def get(self):
        return LocationSendMessage(self.base_url, self.alt_text, self.base_size, self.actions)
