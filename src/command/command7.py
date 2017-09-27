from .command import Command


class Command7(Command):

    def __init__(self):
        self.event = None
        self.command = '7'
        self.template = None
        self.message = None

    def isisValidCmd(self):
        return self.event.message.text == self.command
