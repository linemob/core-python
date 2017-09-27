from .command import Command


class Command4(Command):

    def __init__(self):
        self.event = None
        self.command = '4'
        self.template = None
        self.message = None

    def isisValidCmd(self):
        return self.event.message.text == self.command
