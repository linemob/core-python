from linebot.models import (
    BaseSize, URIImagemapAction, MessageImagemapAction, ImagemapArea
)
from .middleware import Middleware


class ImagemapSendMessageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command9'):
            command.set_message({'base_url': 'https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX17605783.jpg',
                                 'alt_text': 'this is an imagemap',
                                 'base_size': BaseSize(height=1040, width=1040),
                                 'actions': [
                                     URIImagemapAction(
                                         link_uri='https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX17605783.jpg',
                                         area=ImagemapArea(
                                             x=0, y=0, width=520, height=1040
                                         )
                                     ),
                                     MessageImagemapAction(
                                         text='hello',
                                         area=ImagemapArea(
                                             x=520, y=0, width=520, height=1040
                                         )
                                     )
                                 ]
                                 })
