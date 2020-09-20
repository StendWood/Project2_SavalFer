# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *


class Warper(pygame.sprite.Sprite):
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


    def show_teleport_prompt(self):
        """
            Check if the warper rect is touching the player rect => Show a prompt to let the player enter a new map
        """

        if self.rect.colliderect(self.game.player.rect):
            self.game.warper_popup_flag = True
            self.game.current_warper = self.name


    def teleport_prompt(self):
        """
            Manage the teleport prompt graphics and blit
        """

        # self.game.screen.blit(self.game.warper_popup_img, )
