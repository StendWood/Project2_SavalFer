# coding: utf-8

# Imports
import pygame

# Additional code
from game.game import Game
from game.login import Login

def main():
    """
        Main loop
    """

    # Create a game object
    game = Game()
    # Launch the login screen
    game.login_screen()
    while game.login_flag:
        # Login screen refresh
        game.login.show_login_screen()
        # Login screen inputs
        game.login.login_input()
    # Game inputs
    while game.running:
        game.run()

if __name__ == "__main__":
    main()
