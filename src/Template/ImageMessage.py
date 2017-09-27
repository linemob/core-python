from linebot.models import (
    ImageSendMessage,
)


class ImageMessage():

    def __init__(self, command):
        self.original_content_url = command.get_message()['original_content_url']
        self.preview_image_url = command.get_message()['preview_image_url']

    def get(self):
        return ImageSendMessage(self.original_content_url,self.preview_image_url)
