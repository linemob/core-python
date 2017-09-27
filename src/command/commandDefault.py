from .command import Command


class CommandDefault(Command):

    def __init__(self):
        self.event = None
        self.command = 'commandDefault'
        self.template = None
        self.message = None

    def isValidCmd(self):
        return self.event.message.text == self.command
