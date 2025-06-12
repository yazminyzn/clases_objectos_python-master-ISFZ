#!/usr/bin/env python

__author__ = "Prof.Ing.Jesús M.R.González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"


class Stream():
    def __init__(self, client):
        self.client = client

    def write(self, message):
        # Send message to client
        pass


class Wifi(Stream):
    def __init__(self):
        pass


class Bluetooth(Stream):
    def __init__(self):
        pass


class LTE(Stream):
    def __init__(self):
        pass


class Dispatcher():
    def __init__(self, client):
        self.stream = Stream(client)

    def send(self, message):
        self.stream.write(message)
