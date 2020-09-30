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
            Let the player drink and set the hydration lvl to 100
        """

        # Set player hydration to the max
        for i in range(len(game.player.status_gauge["hydration"])):
            game.player.status_gauge["hydration"][i] = 20
        return "You feel refreshed"

    @staticmethod
    def refill(game):
        return "Bottle is refilled"
