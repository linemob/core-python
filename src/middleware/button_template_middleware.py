from linebot.models import (
    ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
from .middleware import Middleware


class ButtonTemplateMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '6'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
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
        command.set_template('TemplateMessageButtonTemplateMiddleware')
