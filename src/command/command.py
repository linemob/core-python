class Command():

    def __init__(self):
        self.event = None
        self.command = None
        self.template = None
        self.message = None

    def set_event(self, event):
        self.event = event

    def get_event(self):
        return self.event

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

    def isValidCmd(self):
        raise NotImplementedError("Please Implement this method")
