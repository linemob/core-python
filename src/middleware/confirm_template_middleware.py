from linebot.models import (
    PostbackTemplateAction, MessageTemplateAction, ConfirmTemplate
)
from .middleware import Middleware


class ConfirmTemplateMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '5'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            command.set_message({'alt_text': 	'Confirm template',
                                 'template': 	ConfirmTemplate(
                                     text='Are you sure?',
                                     actions=[
                                         PostbackTemplateAction(
                                             label='postback',
                                             text='postback text',
                                             data='action=buy&itemid=1'
                                         ),
                                         MessageTemplateAction(
                                             label='message',
                                             text='message text'
                                         )
                                     ]
                                 )
                                 })
            command.set_template('TemplateMessage')
