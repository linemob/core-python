class DefaultMessageMiddleware():

    def __init__(self):
        self.next = True

    def next(self):
        return self.next

    def execute(self, command):
        if(command.get_command() == 'commandDefault'):
            message = "Press Number for order\n1.TextMessage\n2.ImageMessage\n3.LocationMessage\n4.StickerMessage\n5.ConfirmTemplate\n6.ButtonTemplate\n7.CarouselTemplate\n8.ImageCarouselTemplate\n9.ImagemapSendMessage"
            command.set_message(message)
