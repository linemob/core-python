class StickerMessageMiddleware():

    def __init__(self):
        self.next = True

    def next(self):
        return self.next

    def execute(self, command):
        if(command.get_command() == 'command4'):
            command.set_message({'package_id':'1',
                                 'sticker_id':'1'})
