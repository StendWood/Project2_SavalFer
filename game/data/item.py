# coding: utf-8

# Imports
from os import name
import pygame
import pytmx

# Additional codes


class Item:
    """
        Create an item using DB data
    """

    def __init__(self, name, attack, item_type, image_path):

        # Name of the item
        self.name = name
        # Attack value
        self.attack = attack
        # Type of item
        self.type = item_type
        # Load the image
        self.image = pygame.image.load(image_path).convert_alpha()

    def __str__(self):
        """
            Override the print method
        """

        return f"\nName: {self.name}\nAttack power: {self.attack}\nType: {self.type}"
