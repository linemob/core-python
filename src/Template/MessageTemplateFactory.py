from .TextTemplate import TextTemplate
from .ImageMessage import ImageMessage
from .LocationMessage import LocationMessage
from .StickerMessage import StickerMessage
from .TemplateMessage import TemplateMessage


class MessageTemplateFactory():

    def __init__(self, command):
        self.command = command
        print(self.command.get_template())
        if self.command.get_template() == 'TextMessage':
            self.template = TextTemplate(self.command).get()
        elif self.command.get_template() == 'ImageMessage':
            self.template = ImageMessage(self.command).get()
        elif self.command.get_template() == 'LocationMessage':
            self.template = LocationMessage(self.command).get()
        elif self.command.get_template() == 'StickerMessage':
            self.template = StickerMessage(self.command).get()
        elif self.command.get_template() == 'TemplateMessage':
            self.template = TemplateMessage(self.command).get()

    def get(self):
        return self.template
