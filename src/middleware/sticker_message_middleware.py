from .middleware import Middleware


class StickerMessageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '4'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            command.set_message({'package_id': '1',
                                 'sticker_id': '1'})
            command.set_template('StickerMessage')
