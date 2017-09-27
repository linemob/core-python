from linebot.models import (
    TextMessage, StickerMessage, LocationMessage, ImageMessage, VideoMessage, AudioMessage
)
from .command import Command


class CommandRegistry():

    def __init__(self, event):
        self.event = event
        self.default_command = None
        self.command_list = list()

    def add_command(self, command):
        self.command_list.append(command)

    def get_command(self):
        if isinstance(self.event.message, TextMessage):
            self.get_text_message_command()
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

    def get_text_message_command(self):
        for command in self.command_list:
            command.set_event(self.event)
            if command.isValidCmd():
                return command
        default_command.set_event(self.event)
        return default_command

    def get_sticker_message_command(self):
        pass

    def get_location_message_command(self):
        pass

    def get_image_message_command(self):
        pass

    def get_video_message_command(self):
        pass

    def get_audio_message_command(self):
        pass

    def set_default_command(self, default_command):
        self.default_command = default_command

    def get_default_command(self):
        return default_command
