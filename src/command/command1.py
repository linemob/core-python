from .command import Command


class Command1(Command):

    def __init__(self):
        self.event = None
        self.command = '1'
        self.template = None
        self.message = None

    def isisValidCmd(self):
        return self.event.message.text == self.command
