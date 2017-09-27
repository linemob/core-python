class Middleware():

    def __init__(self, command):
        self.do_next = True

    def next(self):
        return self.do_next

    def execute(self, command):
        pass
