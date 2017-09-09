from linebot.models import (
    TextSendMessage,
)


class TextTemplate():

    def __init__(self, command):
        self.text = command.event.message.text

    def get(self):
        return TextSendMessage(self.text)
