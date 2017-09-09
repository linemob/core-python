from .TextTemplate import TextTemplate


class MessageTemplateFactory():

    def __init__(self, command):
        self.command = command
        if(self.command.get_template() == 'TextTemplate'):
            self.template = TextTemplate(self.command).get()

    def get(self):
        return self.template
