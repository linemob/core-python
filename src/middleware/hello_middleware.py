from .middleware import Middleware


class HelloMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '1'

    def execute(self, command):
    	print ('command in hello:'+command.get_command())
        if(command.get_command() == self.middleware_command):
            command.set_message('Hello! World')
            command.set_template('TextMessage')
            print ('command.get_command() == self.middleware_command')
