# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *


class Wall(pygame.sprite.Sprite):
    """
        Manage the game boundraries
    """

    def __init__(self, rect, game):
        # Init the parent sprite class
        pygame.sprite.Sprite.__init__(self)
        # give acces to the game
        self.game = game
        # Set the rect
        self.rect = rect


    def debug_show_wall(self):
        """
            Debug show rect
        """

        pygame.draw.rect(self.game.screen, (255, 0, 0), self.game.camera.apply_rect(self.rect), 2)
