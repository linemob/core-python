class YouSaidMiddleware():

    def __init__(self, command):
        self.command = command

    def next(self):
        self.execute()
        return True

    def execute(self):
        if(self.command.get_command() == 'command1'):
            self.command.event.message.text = 'You said : ' + self.command.event.message.text
            print (self.command.event.message.text)
