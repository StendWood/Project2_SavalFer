# coding: utf-8

# Imports
import socket
from game.config import *


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            # Try to connect to the server
            self.client.connect(self.addr)
            # Return what the server send
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            # Didn't connect to the server
            print(e)

    def send(self, data):
        try:
            # Send data to the server
            self.client.send(str.encode(data))
            # Return the server response
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


