from .middleware import Middleware


class HelloMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '1'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            command.set_message('Hello! World!!')
            command.set_template('TextMessageNAAA')
            print('hellomiddleware message:' + command.get_message())
            print('hellomiddleware template:' + command.get_template())
