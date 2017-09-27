from linebot.models import (
    TemplateSendMessage,
)


class TemplateMessage():

    def __init__(self, command):
        self.alt_text = command.get_message()['alt_text']
        self.template = command.get_message()['template']

    def get(self):
        return TemplateSendMessage(self.alt_text, self.template)
