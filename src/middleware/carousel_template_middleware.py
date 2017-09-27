from linebot.models import (
    CarouselTemplate, CarouselColumn, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
from .middleware import Middleware


class CarouselTemplateMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '7'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            command.set_message({'alt_text': 'Carousel template',
                                 'template': CarouselTemplate(
                                     columns=[
                                         CarouselColumn(
                                             thumbnail_image_url='https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                             title='this is menu1',
                                             text='description1',
                                             actions=[
                                                 PostbackTemplateAction(
                                                     label='postback1',
                                                     text='postback text1',
                                                     data='action=buy&itemid=1'
                                                 ),
                                                 MessageTemplateAction(
                                                     label='message1',
                                                     text='message text1'
                                                 ),
                                                 URITemplateAction(
                                                     label='uri1',
                                                     uri='https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg'
                                                 )
                                             ]
                                         ),
                                         CarouselColumn(
                                             thumbnail_image_url='https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                             title='this is menu2',
                                             text='description2',
                                             actions=[
                                                 PostbackTemplateAction(
                                                     label='postback2',
                                                     text='postback text2',
                                                     data='action=buy&itemid=2'
                                                 ),
                                                 MessageTemplateAction(
                                                     label='message2',
                                                     text='message text2'
                                                 ),
                                                 URITemplateAction(
                                                     label='uri2',
                                                     uri='https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg'
                                                 )
                                             ]
                                         )
                                     ]
                                 )

                                 })
            command.set_template('TemplateMessage')
