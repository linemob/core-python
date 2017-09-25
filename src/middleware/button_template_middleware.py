from linebot.models import (
    ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
from .middleware import Middleware


class ButtonTemplateMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command6'):
            command.set_message({'alt_text': 'Buttons template',
                                 'template': ButtonsTemplate(
                                     thumbnail_image_url='https://example.com/image.jpg',
                                     title='Menu',
                                     text='Please select',
                                     actions=[
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
                                             uri='http://example.com/'
                                         )
                                     ]
                                 )
                                 })
