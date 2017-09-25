from linebot.models import (
    ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
from .middleware import Middleware


class ButtonTemplateMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command6'):
            command.set_message({'thumbnail_image_url': 'https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                 'title': 'Menu',
                                 'text': 'Please Select',
                                 'actions': [
                                     PostbackTemplateAction(
                                         label='postback',
                                         text='postback text',
                                         data='action=buy&itemid=1'
                                     ),
                                     MessageTemplateAction(
                                         label='message',
                                         text='message text'
                                     ),
                                     URITemplateAction(
                                         label='uri',
                                         uri='http://www.google.com/'
                                     )
                                 ]
                                 })
