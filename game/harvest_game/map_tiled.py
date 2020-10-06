
import pygame
import pytmx


from pygame_utilities import Pygame_util


class Map_tiled():
    """
        manages tiled
    """

    # pygame.init()
    # screen = pygame.display.set_mode((800,600))

    @staticmethod
    def render(surface: pygame.Surface, image_link):
        """
            Take a surface and draw the tilemap on them
        """
        tmxdata = pytmx.load_pygame(image_link, pixelalpha=True)
        # Save the command to a lower size
        # ti = tmxdata.get_tile_image #_by_gid
        layers = tmxdata.visible_layers
        # Check every layer in the visible layers
        for layer in layers:
            # Check for a tiled layer
            # if isinstance(layer, pytmx.TiledTileLayer):
            #     # Get the pos(x, y) and the gid
            for x, y, gid, in layer:
                tile = tmxdata.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tmxdata.tilewidth, 
                                        y * tmxdata.tileheight))

