from .middleware.hello_middleware import HelloMiddleware
from .middleware.button_template_middleware import ButtonTemplateMiddleware
from .middleware.carousel_template_middleware import CarouselTemplateMiddleware
from .middleware.confirm_template_middleware import ConfirmTemplateMiddleware
from .middleware.default_message_middleware import DefaultMessageMiddleware
from .middleware.image_carousel_template_middleware.py import ImageCarouselTemplateMiddleware
from .middleware.image_message_middleware import ImageMiddleware
from .middleware.imagemap_send_message_middleware import ImagemapSendMessageMiddleware
from .middleware.location_message_middleware import LocationMessageMiddleware
from .middleware.sticker_message_middleware import StickerMessageMiddleware
from .handler import Handler


class CommandBus():

    def __init__(self, command):
        self.command = command
        self.middleware = list()
        self.initial()
        self.run()

    def initial(self):
        self.add(HelloMiddleware())
        self.add(ButtonTemplateMiddleware())
        self.add(CarouselTemplateMiddleware())
        self.add(ConfirmTemplateMiddleware())
        self.add(DefaultMessageMiddleware())
        self.add(ImageCarouselTemplateMiddleware())
        self.add(ImageMiddleware())
        self.add(LocationMessageMiddleware())
        self.add(StickerMessageMiddleware())
        self.add(ImagemapSendMessageMiddleware())


    def add(self, middleware):
        self.middleware.append(middleware)

    def get(self, index):
        return self.middleware[index]

    def run(self):
        for middleware in self.middleware:
            middleware.execute(self.command)
            if(not middleware.next()):
                break
        handler = Handler(self.command)
