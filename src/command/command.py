class Command():

    def __init__(self, event, command, template):
        self.event = event
        self.command = command
        self.template = template
        self.message = None

    def set_command(selt, command):
        self.command = command

    def get_command(self):
        return self.command

    def set_template(self, template):
        self.template = template

    def get_template(self):
        return self.template

    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message
