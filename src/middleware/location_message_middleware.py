from .middleware import Middleware


class LocationMessageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '3'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            print('in LocationMessageMiddleware ')
            command.set_message({'title': 'my location',
                                 'address': 'Tokyo',
                                 'latitude': '35.65910807942215',
                                 'longitude': '139.70372892916203'})
            command.set_template('LocationMessage')
