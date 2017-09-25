from .TextTemplate import TextTemplate
from .ImageMessage import ImageMessage
from .LocationMessage import LocationMessage
from .StickerMessage import StickerMessage
from .TemplateMessage import TemplateMessage


class MessageTemplateFactory():

    def __init__(self, command):
        self.command = command
        if self.command.get_template() == 'TextTemplate':
            self.template = TextTemplate(self.command).get()
        elif self.command.get_template() == 'ImageMessage':
            self.template = ImageMessage(self.command).get()
        elif self.command.get_template() == 'LocationMessage':
            self.template = LocationMessage(self.command).get()
        elif self.command.get_template() == 'StickerMessage':
            self.template = StickerMessage(self.command).get()
        elif self.command.get_template() == 'TemplateMessage':
            self.template = TemplateMessage(self.command).get()
        else:
            self.command = Command(
                self.event, 'commandDefault', 'TextTemplate')

    def get(self):
        return self.template
