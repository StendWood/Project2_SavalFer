# coding: utf-8

# Imports
import pygame
import pytmx

# Additional code
from game.config import *


class Map:
    """
        Handle the game map | Load, render
    """

    def __init__(self, filename: str):
        # Load the map | Pixel alpha mean transparency is ON
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        # Setup the width and height
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        # Save those data
        self.tmxdata = tm


    def render(self, surface: pygame.Surface):
        """
            Take a surface and draw the tilemap on them
        """

        # Save the command to a lower size
        ti = self.tmxdata.get_tile_image_by_gid
        layers = self.tmxdata.visible_layers
        # Check every layer in the visible layers
        for layer in layers:
            # Check for a tiled layer
            if isinstance(layer, pytmx.TiledTileLayer):
                # Get the pos(x, y) and the gid
                for x, y, gid, in layer:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, 
                                            y * self.tmxdata.tileheight))


    def make_map(self):
        """
            Create a surface and call the render method
        """
        # Create a surface the size of the map (pygame.SRCALPHA enable transparency for the surface)
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Render the map on the temp_surface
        self.render(temp_surface)
        return temp_surface


    @staticmethod
    def map_loader(game):
        """
            Load every map of the game
        """

        # Give access to game
        game = game
# Load the maps
    # WORLDMAP
        game.maps["worldmap"]["map"] = Map("assets/maps/world_map/world_map.tmx")
        game.maps["worldmap"]["foreground"] = Map("assets/maps/world_map/world_map_foreground.tmx")
# Create the maps image
    # WORLDMAP
        game.maps["worldmap"]["img"] = game.maps["worldmap"]["map"].make_map()
        game.maps["worldmap"]["fg_img"] = game.maps["worldmap"]["foreground"].make_map()
# Create the maps rect
    # WORLDMAP
        game.maps["worldmap"]["rect"] = game.maps["worldmap"]["img"].get_rect()
