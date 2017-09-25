from linebot.models import (
    TextMessage, StickerMessage, LocationMessage, ImageMessage, VideoMessage, AudioMessage
)
from .command import Command


class CommandRegistry():

    def __init__(self, event):
        self.event = event
        self.command = None
        self.check()

    def get_command(self):
        return self.command

    def check(self):
        if isinstance(self.event.message, TextMessage):
            self.set_text_message_command()
        elif isinstance(self.event.message, StickerMessage):
            pass
        elif isinstance(self.event.message, LocationMessage):
            pass
        elif isinstance(self.event.message, ImageMessage):
            pass
        elif isinstance(self.event.message, VideoMessage):
            pass
        elif isinstance(self.event.message, AudioMessage):
            pass
        else:
            self.set_default_message_command()

    def set_text_message_command(self):
        text = self.event.message.text
        if text == '1':
            self.command = Command(self.event, 'command1', 'TextMessage')
        elif text == '2':
            self.command = Command(self.event, 'command2', 'ImageMessage')
        elif text == '3':
            self.command = Command(self.event, 'command3', 'LocationMessage')
        elif text == '4':
            self.command = Command(self.event, 'command4', 'StickerMessage')
        elif text == '5':
            self.command = Command(self.event, 'command5', 'TemplateMessage')
        elif text == '6':
            self.command = Command(self.event, 'command6', 'TemplateMessage')
        elif text == '7':
            self.command = Command(self.event, 'command7', 'TemplateMessage')
        elif text == '8':
            pass
        elif text == '9':
            self.command = Command(
                self.event, 'command9', 'TemplateMessage')
        else:
            self.command = Command(
                self.event, 'commandDefault', 'TextMessage')

    def set_sticker_message_command(self):
        pass

    def set_location_message_command(self):
        pass

    def set_image_message_command(self):
        pass

    def set_video_message_command(self):
        pass

    def set_audio_message_command(self):
        pass

    def set_default_message_command(self):
        self.command.set('default')
