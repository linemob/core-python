from .middleware import Middleware


class HelloMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '1'

    def execute(self, command):
        print('command in hello:' + command.get_command())
        if(command.get_command() == self.middleware_command):
            command.set_message('Hello! World pawa')
            command.set_template('TextMessage')
            print('command.get_command() == self.middleware_command')
            print('hellomiddleware message:' + command.get_message())
            print('hellomiddleware template:' + command.get_template())
