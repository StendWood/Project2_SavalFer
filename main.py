# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *
from game.game import Game

def main():
    """
        Main loop
    """

    # Create a game object
    game = Game()
    # Load the config
    game.load_cfg()
    # Manage cfg loading errors
    if not game.load_cfg_error:
        # Launch the login screen
        game.login_screen()
        while game.login_flag:
            # Login screen refresh
            game.login.show_login_screen()
            # Login screen inputs
            game.login.login_input()
        # Game inputs
        while game.running:
            ###########################################
            #   HORRID CODE DON'T DO THIS AT HOME     #
            ###########################################
            game.screen.fill(BLACK)                   #
            game.screen.blit(pygame.image.load("img/bg/map-1.png"),(0, 50))
            pygame.display.flip()                     #
            ###########################################
            ###########################################
            game.run()

if __name__ == "__main__":
    main()
