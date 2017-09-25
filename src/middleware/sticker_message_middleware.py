from .middleware import Middleware


class StickerMessageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True

    def execute(self, command):
        if(command.get_command() == 'command4'):
            command.set_message({'package_id': '1',
                                 'sticker_id': '1'})
