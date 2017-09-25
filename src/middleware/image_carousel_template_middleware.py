from linebot.models import (
    ImageCarouselTemplate, ImageCarouselColumn, PostbackTemplateAction
)


class ImageCarouselTemplateMiddleware():

    def __init__(self):
        self.next = True

    def next(self):
        return self.next

    def execute(self, command):
        if(command.get_command() == 'command8'):
            command.set_message({'alt_text'='ImageCarousel template',
                                 'template'=ImageCarouselTemplate(
                                     columns=[
                                         ImageCarouselColumn(
                                             image_url='https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                             action=PostbackTemplateAction(
                                                 label='postback1',
                                                 text='postback text1',
                                                 data='action=buy&itemid=1'
                                             )
                                         ),
                                         ImageCarouselColumn(
                                             image_url='https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                             action=PostbackTemplateAction(
                                                 label='postback2',
                                                 text='postback text2',
                                                 data='action=buy&itemid=2'
                                             )
                                         )
                                     ]
                                 )
                                 })
