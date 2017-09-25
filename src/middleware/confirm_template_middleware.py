from linebot.models import (
    PostbackTemplateAction, MessageTemplateAction, ConfirmTemplate
)


class ConfirmTemplateMiddleware():

    def __init__(self):
        self.next = True

    def next(self):
        return self.next

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
