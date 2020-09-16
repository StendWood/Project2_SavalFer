# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *


class Camera:
    """
        Init the camera
    """

    def __init__(self, width, height):
        # Check the offset to move
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height


    def apply(self, shit_to_move):
        """
            Apply the camera offset to an object
        """

        return shit_to_move.rect.move(self.camera.topleft)


    def apply_rect(self, rect):
        return rect.move(self.camera.x, self.camera.y)


    def apply_parallax(self, rect, layer):
        """
            Manage the parallax shift
        """

        # Clouds
        if layer == 5:
            return rect.move(self.camera.x*0.10, self.camera.y*0.10)
        # Far
        if layer == 4:
            return rect.move(self.camera.x*0.15, self.camera.y*0.15)
        # Middle
        if layer == 3:
            return rect.move(self.camera.x*0.25, self.camera.y*0.25)
        # Close
        if layer == 2:
            return rect.move(self.camera.x*0.55, self.camera.y*0.55)
        # Super close
        if layer == 1:
            return rect.move(self.camera.x*0.85, self.camera.y*0.85)


    def update(self, target):
        """
            Follow a target (Most likely the player)
        """

        x = (-target.rect.x + WIDTH / 2)
        y = (-target.rect.y + HEIGHT / 2)
        # Limit x and y
        x = min(0, x) # Left
        y = min(0, y) # Top
        x = max(-(self.width - WIDTH), x) # Right
        y = max(-(self.height - HEIGHT), y) # Bottom
        # Update the camera rect
        self.camera = pygame.Rect(x , y, self.width, self.height)
