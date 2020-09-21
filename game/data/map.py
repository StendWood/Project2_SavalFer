# coding: utf-8

# Imports
import pygame
import pytmx

# Additional code
from game.config import *
from game.player import Player
from game.obstacles import Wall
from game.warper import Warper


class Map:
    """
        Handle the game map | Load, render, transition
    """

    def __init__(self, filename: str, game):
        # Load the map | Pixel alpha mean transparency is ON
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.game = game
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


    def make(self):
        """
            Create a surface and call the render method
        """
        # Create a surface the size of the map (pygame.SRCALPHA enable transparency for the surface)
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Render the map on the temp_surface
        self.render(temp_surface)
        return temp_surface


    def create_obstacles_n_warpers(self, map_name, create_player: bool=False, move_player: bool=True):
        # Generate the player / walls  / warpers
        for tile_object in self.game.maps[map_name]["map"].tmxdata.objects:
            # Spawn the player
            if tile_object.name == "player":
                if create_player:
                    self.game.player = Player(tile_object.x, tile_object.y, "img/avatar/1/", self.game)
                    self.game.all_sprites.add(self.game.player)
                    print("Player created.")
                elif move_player:
                    self.game.player.rect.x, self.game.player.rect.y = tile_object.x, tile_object.y
                    print("Player moved.")
            # Spawn the walls
            if tile_object.name == "wall":
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.game.walls.add(Wall(rect, self.game))
            # Spawn the warpers
            if "warper" in tile_object.name:
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                # Create a temp warpers
                temp_warper = Warper(rect, self.game)
                # Add the name
                setattr(temp_warper, "name", tile_object.name.split("_")[0])
                # Save the warper in the sprite group
                self.game.warpers.add(temp_warper)
                print("Warper created.")


    def transition(self, map_name):
        """
            Manage the transition screen during the map load
        """

        # Show the loading background
        self.game.screen.blit(self.game.maps[map_name]["loading"], (0, 0))
        pygame.display.update()
        # Remove the last map obstacles ans warpers
        self.game.walls.empty()
        self.game.warpers.empty()
        # Create the new map obstacles, warpers and move the player
        self.create_obstacles_n_warpers(map_name)


    @staticmethod
    def loader(game):
        """
            Load every map of the game
        """

        # Give access to game
        game = game
# Load the maps
    # EdWorld
        game.maps["worldmap"]["map"] = Map("assets/maps/world_map/world_map.tmx", game)
        game.maps["worldmap"]["foreground"] = Map("assets/maps/world_map/world_map_foreground.tmx", game)
    # EDWORLD
        game.maps["EdWorld"]["map"] = Map("assets/maps/EdWorld/edworld.tmx", game)
# Create the maps image
    # WORLDMAP
        game.maps["worldmap"]["img"] = game.maps["worldmap"]["map"].make()
        game.maps["worldmap"]["fg_img"] = game.maps["worldmap"]["foreground"].make()
    # EDWORLD
        game.maps["EdWorld"]["img"] = game.maps["EdWorld"]["map"].make()
        # game.maps["EdWorld"]["fg_img"] = game.maps["EdWorld"]["foreground"].make()
# Create the maps rect
    # WORLDMAP
        game.maps["worldmap"]["rect"] = game.maps["worldmap"]["img"].get_rect()
    # EDWORLD
        game.maps["EdWorld"]["rect"] = game.maps["EdWorld"]["img"].get_rect()
# Load the maps loading background
    # WORLDMAP
        game.maps["worldmap"]["loading"] = pygame.image.load("img/login/login_bg.jpg")
    # EDWORLD
        game.maps["EdWorld"]["loading"] = pygame.image.load("img/loading/EdWorld/Edworld.png")
        
