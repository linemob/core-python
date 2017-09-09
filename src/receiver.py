from .command.command_registry import CommandRegistry
from .command_bus import CommandBus


class Receiver():

    def __init__(self, event):
        self.event = event
        command_registry = CommandRegistry(self.event)
        command = command_registry.get_command()
        command_bus = CommandBus(command)
