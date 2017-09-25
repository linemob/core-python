from .middleware import Middleware


class HelloMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command1'):
            command.set_message('Hello! World')
