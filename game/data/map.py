# coding: utf-8

# Imports
import pygame
import pytmx

# Additional code
from game.config import *
from game.player import Player
from game.obstacles import Wall
from game.warper import Warper
from game.pnj import Pnj
from game.water_source import Water_source


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

    def create_map_objects(self, map_name, create_player: bool = False, move_player: bool = True, old_pos: bool = False):
        # Generate the player / walls  / warpers
        for tile_object in self.game.maps[map_name]["map"].tmxdata.objects:
            # Spawn the player
            if tile_object.name == "player":
                if create_player:
                    self.game.player = Player(tile_object.x, tile_object.y, "assets/img/avatar/1/", self.game)
                    self.game.all_sprites.add(self.game.player)
                elif move_player:
                    # Move the player
                    if not old_pos:
                        self.game.player.rect.x, self.game.player.rect.y = tile_object.x, tile_object.y
                    else:
                        self.game.player.rect.x, self.game.player.rect.y = self.game.player.old_pos[0], self.game.player.old_pos[1]
            # Spawn the walls
            if tile_object.name == "wall":
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.game.walls.add(Wall(rect, self.game))
            # Spawn the warpers
            try:
                if "warper" in tile_object.name:
                    # Create the rect
                    rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                    # Create a temp warpers
                    temp_warper = Warper(rect, self.game)
                    # Add the name
                    setattr(temp_warper, "name", tile_object.name.split("_")[0])
                    # Save the warper in the sprite group
                    self.game.warpers.add(temp_warper)
            except TypeError as e:
                print(e)
            # Spawn the PNJ
            if "pnj" in tile_object.name:
                # Create the rect
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                # Extract the attributes values
                attrib_values = tile_object.name.split("_")
                # Create and save the pnj in the Pnj sprite group
                self.game.pnj.add(Pnj(attrib_values[0], attrib_values[1], rect, self.game))
            # Spawn water supplies
            if "water" in tile_object.name:
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.game.water_sources.add(Water_source(rect, self.game))

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
        self.game.pnj.empty()
        # Create the new map obstacles, warpers and move the player
        if self.game.player.current_map != "worldmap":
            self.create_map_objects(map_name)
        else:
            self.create_map_objects(map_name, old_pos=True)

    @staticmethod
    def loader(game):
        """
            Load every map of the game
        """

        # Give access to game
        game = game
        # Load the maps
        # WorldMap
        game.maps["worldmap"]["map"] = Map("assets/maps/world_map/world_map.tmx", game)
        game.maps["worldmap"]["foreground"] = Map("assets/maps/world_map/world_map_foreground.tmx", game)
        # EDWORLD
        game.maps["EdWorld"]["map"] = Map("assets/maps/EdWorld/edworld.tmx", game)
        # GardenLand
        game.maps["GardenLand"]["map"] = Map("assets/maps/GardenLand/gardenland.tmx", game)
        game.maps["GardenLand"]["foreground"] = Map("assets/maps/GardenLand/gardenland_foreground.tmx", game)
        # ! Pick_food
        game.maps["pick_food"]["map"] = Map("assets/maps/pick_food/pick_food.tmx",game)
        
        # Create the maps image
        # WORLDMAP
        game.maps["worldmap"]["img"] = game.maps["worldmap"]["map"].make()
        game.maps["worldmap"]["fg_img"] = game.maps["worldmap"]["foreground"].make()
        # EDWORLD
        game.maps["EdWorld"]["img"] = game.maps["EdWorld"]["map"].make()
        # game.maps["EdWorld"]["fg_img"] = game.maps["EdWorld"]["foreground"].make()
        # GardenLand
        game.maps["GardenLand"]["img"] = game.maps["GardenLand"]["map"].make()
        game.maps["GardenLand"]["fg_img"] = game.maps["GardenLand"]["foreground"].make()
        # !  Pick_food
        game.maps["pick_food"]["img"] = game.maps["pick_food"]["map"].make()
        
        # Create the maps rect
        # WORLDMAP
        game.maps["worldmap"]["rect"] = game.maps["worldmap"]["img"].get_rect()
        # EDWORLD
        game.maps["EdWorld"]["rect"] = game.maps["EdWorld"]["img"].get_rect()
        # GardenLand
        game.maps["GardenLand"]["rect"] = game.maps["GardenLand"]["img"].get_rect()
        # !  Pick_food
        game.maps["pick_food"]["rect"] = game.maps["pick_food"]["img"].get_rect()
        
        # Load the maps loading background
        # WORLDMAP
        game.maps["worldmap"]["loading"] = pygame.image.load("assets/img/login/login_bg.jpg")
        # EDWORLD
        game.maps["EdWorld"]["loading"] = pygame.image.load("assets/img/loading/EdWorld/Edworld.png")
        # GardenLand
        game.maps["GardenLand"]["loading"] = pygame.image.load("assets/img/loading/GardenLand.png")
        # !  Pick_food
        game.maps["pick_food"]["loading"] = pygame.image.load("img/loading/pick_food/pick_food.png")
        