from linebot.models import (
    LocationSendMessage,
)


class LocationMessage():

    def __init__(self, command):
        self.title = command.get_message()['title']
        self.address = command.get_message()['address']
        self.latitude = command.get_message()['latitude']
        self.longitude = command.get_message()['longitude']

    def get(self):
        return LocationSendMessage(self.title, self.address, self.latitude, self.longitude)
