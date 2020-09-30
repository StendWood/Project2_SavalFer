# coding: utf-8

# Imports
import pygame
from typing import Type

# Additional code
from game.config import *


class Gui:
    """
        Game GUI
    """

    gui_images = {
        "health" : [],
        "hydration" : [],
        "satiety" : [],
    }
    health_gui_path = "assets/gui/health/health_"
    hydration_gui_path = "assets/gui/hydration/hydration_"
    satiety_gui_path = "assets/gui/satiety/satiety_"

    @classmethod
    def load_gui_image(cls, status: str, img_path: str):
        """
            Load the GUI images
        """

        # Iterate the sataus images
        for i in range(5):
            # Load the 5 images
            cls.gui_images[status].append(pygame.image.load(f"{img_path}{i}.png").convert_alpha())

    @classmethod
    def show_gui(cls, game):
        """
            Show the hydration, satiety and health bar depending on their current level
        """

        # Set the base x-coordinate and y-coodinate
        x = 10
        y = 10
        for gauge in game.player.status_gauge.items():
            # Check every status vial
            for stats_vial in gauge[1]:
                # Calculate the current % for each vial
                game.screen.blit(cls.gui_images[gauge[0]][stats_vial//5], (x, y))
                # Increment x-coordinate
                if gauge[0] in ["health", "satiety"]:
                    x += 30
                else:
                    x += 20
            x += 75

