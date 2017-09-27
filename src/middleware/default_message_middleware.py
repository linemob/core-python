from .middleware import Middleware


class DefaultMessageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = 'commandDefault'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            message = "************\nPress Number for order\n1.TextMessage\n2.ImageMessage\n3.LocationMessage\n4.StickerMessage\n5.ConfirmTemplate\n6.ButtonTemplate\n7.CarouselTemplate\n************"
            command.set_message(message)
            command.set_template('TextMessage')
            print('in DefaultMessageMiddleware ')
