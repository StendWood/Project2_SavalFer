# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *


class Water_source(pygame.sprite.Sprite):
    """
        Manage the different map teleporter (change the current map)
    """

    def __init__(self, rect, game):
        # Init the parent sprite class
        pygame.sprite.Sprite.__init__(self)
        # Give acces to the game
        self.game = game
        # Set the rect
        self.rect = rect

    @staticmethod
    def drink(game):
        """
            Let the player drink and set the hydratation lvl to 100
        """

        # Set player hydratation to the max
        if game.player.hydratation < 100:
            game.player.hydratation = 100
        return "You feel refreshed"

    @staticmethod
    def refill(game):
        return "Bottle is refilled"
