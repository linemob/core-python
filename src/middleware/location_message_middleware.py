from .middleware import Middleware


class LocationMessageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command3'):
            command.set_message({'title': 'my location',
                                 'address': 'Tokyo',
                                 'latitude': '35.65910807942215',
                                 'longitude': '139.70372892916203'})
