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
        # Rect
        self.rect = self.image.get_rect()
        # Tooltip
        if self.attack != 0:
            self.tooltip = [f"{self.name}", f"Attack: {self.attack}", f"Type: {self.type}"]
        else:
            self.tooltip = [f"{self.name}", f"Type: {self.type}"]

    def __str__(self):
        """
            Override the print method
        """

        return f"\nName: {self.name}\nAttack power: {self.attack}\nType: {self.type}"



