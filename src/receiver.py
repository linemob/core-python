from .command.command_registry import CommandRegistry
from .command.command1 import Command1
from .command.command2 import Command2
from .command.command3 import Command3
from .command.command4 import Command4
from .command.command5 import Command5
from .command.command6 import Command6
from .command.command7 import Command7
from .command.commandDefault import CommandDefault
from .command_bus import CommandBus


class Receiver():

    def __init__(self, event):
        self.event = event
        command_registry = CommandRegistry(self.event)
        command_registry.add_command(Command1())
        command_registry.add_command(Command2())
        command_registry.add_command(Command3())
        command_registry.add_command(Command4())
        command_registry.add_command(Command5())
        command_registry.add_command(Command6())
        command_registry.add_command(Command7())
        command_registry.add_command(CommandDefault())
        command_bus = CommandBus(command_registry.get_command())
