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
        if text == 'hello':
            self.command = Command(self.event, 'command1', 'TextTemplate')
        elif text == 'goodbye':
            self.command = Command(self.event, 'command2', 'TextTemplate')

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
