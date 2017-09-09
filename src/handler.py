from linebot import (
    LineBotApi, WebhookHandler
)

from .Template.MessageTemplateFactory import MessageTemplateFactory


class Handler():

    def __init__(self, command):
        self.command = command
        self.template = MessageTemplateFactory(command).get()
        self.sendMessage()

    def sendMessage(self):
        line_bot_api = LineBotApi(
            'xJBvxhncO6zH7t/Hsynzv9Dq6ODqrc+lMZb3ZzcObJV6fPSttweWZ6qAvNWrQ0aJ6GPaUP5JOBHcbRctlLKDd6NRo65Dp81luK57sQ33sB2gVaKlAQ8I6rGMs0/uLuztQIku+cF70s5ZomBKClrR/gdB04t89/1O/w1cDnyilFU=')
        if(self.command.get_template() == 'TextTemplate'):
            line_bot_api.reply_message(
                self.command.event.reply_token, self.template)
