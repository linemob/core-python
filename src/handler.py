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
            'hMMdUsmj1Mq7JmTo3x0gCh/L6WilPgxU5UfCEh24aHQNad8NOAMu8+4XdaKgFMzcG4nO+CSf/vVHMJ+4MvtBLV+akhxxXChn3X5tD0dPE+M/ixVqml7WFi2baNlzz7izNNXmL4LlnL56eZs1Dh4m9QdB04t89/1O/w1cDnyilFU=')
        line_bot_api.reply_message(
            self.command.event.reply_token, self.template)
