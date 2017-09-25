from linebot.models import (
    PostbackTemplateAction, MessageTemplateAction, ConfirmTemplate
)
from .middleware import Middleware


class ConfirmTemplateMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command5'):
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
