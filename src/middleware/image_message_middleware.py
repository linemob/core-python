from .middleware import Middleware


class ImageMiddleware(Middleware):

    def __init__(self):
        self.do_next = True
        self.middleware_command = '2'

    def execute(self, command):
        if(command.get_command() == self.middleware_command):
            command.set_message({'original_content_url': 'https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                 'preview_image_url': 'https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg'})
            command.set_template('ImageMessage')
