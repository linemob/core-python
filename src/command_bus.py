from .middleware.you_said_middleware import YouSaidMiddleware
from .handler import Handler


class CommandBus():

    def __init__(self, command):
        self.command = command
        self.middleware = list()
        self.initial()
        self.run()

    def initial(self):
        self.add(YouSaidMiddleware(self.command))

    def add(self, middleware):
        self.middleware.append(middleware)

    def get(self, index):
        return self.middleware[index]

    def run(self):
        for middleware in self.middleware:
            if(not middleware.next()):
                break
        handler = Handler(self.command)
