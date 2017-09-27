from .command import Command


class Command6(Command):

    def __init__(self):
        self.event = None
        self.command = '6'
        self.template = None
        self.message = None

    def isValidCmd(self):
        return self.event.message.text == self.command
