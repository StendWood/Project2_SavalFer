# coding: utf-8

# Imports
import socket
from _thread import *
from s_config import *

class Server:
    """
        Manage the communication between the players and the database.
    """

    def __init__(self):
        self.server = SERVER
        self.port = PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((SERVER, PORT))
        except socket.error as e:
            print(e)

        self.s.listen(9)
        print("Server started.")
        print("Waiting for connection.")

        # Game data
        self.game_data = {}

server = Server()
while True:
    conn, addr = server.s.accept()
    print("\nConnected to :", addr)
