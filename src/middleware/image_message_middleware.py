class ImageMiddleware():

    def __init__(self):
        self.next = True

    def next(self):
        return self.next

    def execute(self, command):
        if(command.get_command() == 'command2'):
            command.set_message({'original_content_url': 'https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg',
                                 'preview_image_url': 'https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg'})
