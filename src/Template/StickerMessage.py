from linebot.models import (
    StickerSendMessage,
)


class StickerMessage():

    def __init__(self, command):
        self.package_id = command.get_message()['package_id']
        self.sticker_id = command.get_message()['sticker_id']

    def get(self):
        return StickerSendMessage(self.package_id, self.sticker_id)
