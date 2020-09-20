# coding: utf-8

# Imports
import pygame
import json

from pygame.constants import KEYUP

# Additional code
from game.config import *
from game.login import Login
from game.player import Player
from game.camera import Camera
from game.data.map import Map
from game.obstacles import Wall
from game.warper import Warper


class Game:
    """
        Main game class
    """

    def __init__(self):
        # Init the config
        self.cfg = {}
        self.load_cfg_error = False
        # Pygame init
        pygame.init()
        # Sound init
        pygame.mixer.init()
        # Font init
        pygame.font.init()
        self.username_font = pygame.font.SysFont(LOGIN_FONT,22)
        self.password_font = pygame.font.SysFont(LOGIN_FONT,16)
        self.login_field_title_font = pygame.font.SysFont(LOGIN_FONT, 30)
        self.validate_button_font = pygame.font.SysFont(VALIDATE_FONT, 25)
        self.login_error_font = pygame.font.SysFont(ERROR_FONT, 15)
        self.warper_font = pygame.font.Font(WARPER_FONT, 22)

        # Create the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Change the window name
        pygame.display.set_caption("SavalFer")

        # Create the clock
        self.clock = pygame.time.Clock()
        self.running = True

        # Key pressed
        self.pressed = {} 

        # Map management
        self.maps = {
            "worldmap" :
                {
                    # Map instance
                    "map" : "",
                    # Map foreground instance
                    "foreground" : "",
                    # Map image
                    "img" : "",
                    # Map foreground image
                    "fg_img" : "",
                    # Map Rect
                    "rect" : "",
                },
            "EdWorld" :
                {
                    # Map instance
                    "map" : "",
                    # Map foreground instance
                    "foreground" : "",
                    # Map image
                    "img" : "",
                    # Map foreground image
                    "fg_img" : "",
                    # Map Rect
                    "rect" : "",
                },
            
        }
        # Flag management
        self.warper_popup_flag = False
        self.current_warper = None
        # self.worldmap_flag = False


    def run(self):
        """
            Game loop | FPS, Event, Update, 
        """

        # Main loop
        # Set playing to true
        self.playing = True
        # Preload the images
        self.image_preloader()
        # Launche the main loop
        while self.playing:
            # Clock the FPS
            self.clock.tick(FPS)
            # Manage inputs depending on the map
            if not self.warper_popup_flag:
                # Popup is not active
                if self.player.current_map == "worldmap":
                    self.worldmap_event()
            elif self.warper_popup_flag:
                # Popup is active
                self.warper_popup_event()
            # Update
            self.update()
            # Draw
            self.draw()


    # WORLDMAP
    def worldmap_event(self):
        """
            Listen and process inputs
        """

        # Process inputs
        for event in pygame.event.get():
            # Quit the game
            self.quit_game(event)
            # Manage the key pressed
            if event.type == pygame.KEYDOWN:
                # Set key bool to True
                self.pressed[event.key] = True
            # Manage key release
            elif event.type == pygame.KEYUP:
                # Spacebar
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                # E
                elif event.key == pygame.K_e:
                    # Check for any teleport to enter
                    for warper in self.warpers:
                        warper.show_teleport_prompt()
                # Reset key bool to False
                self.pressed[event.key] = False

        # Manage movements inputs
        # check if the player want to go to the right
        if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d):
            # Check for collisions and move the player
            self.player.move("run_side", "right")
        # check if the player want to go to the left
        if self.pressed.get(pygame.K_LEFT)or self.pressed.get(pygame.K_q):
            # Check for collisions and move the player
            self.player.move("run_side", "left", True)
        # check if the player want to go up
        if self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_z):
            # Check for collisions and move the player
            self.player.move("run_up", "up")
        # check if the player want to go down
        if self.pressed.get(pygame.K_DOWN) or self.pressed.get(pygame.K_s):
            # Check for collisions and move the player
            self.player.move("run_down", "down")

        # Reset animation when idle
        if all(not value for value in self.pressed.values()) and self.player.status not in ["idle_up", "idle_down"]:
            # If no key is pressed and status is not idle
            if self.player.status == "run_up":
                self.player.change_action("idle_up")
            elif self.player.status == "run_down":
                self.player.change_action("idle_down")
            elif self.player.status == "run_side":
                self.player.change_action("idle_side")


    def draw(self):
        """
            Draw the elements of the map and refresh the screen
        """

        # FPS counter
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # Map
        self.screen.blit(
                        # Use the current map img
                        self.maps[self.player.current_map]["img"],
                        # Apply the scrolling
                        self.camera.apply_rect(
                            # Use the current map rect
                            self.maps[self.player.current_map]["rect"])
                        )
        # Draw every sprites (Player and monsters)
        for sprite in self.all_sprites:
            if self.player.flip:
                self.screen.blit(pygame.transform.flip(sprite.image, True, False), 
                                self.camera.apply_rect(sprite.rect))
            else:
                self.screen.blit(sprite.image, self.camera.apply_rect(sprite.rect))
        # Map foreground
        self.screen.blit(self.maps[self.player.current_map]["fg_img"], 
                        self.camera.apply_rect(self.maps[self.player.current_map]["rect"]))

        if self.warper_popup_flag:
            # Show the popup background
            self.screen.blit(self.warper_popup_img, (250, 450))
            # Blit the text
            self.screen.blit(self.warper_font.render("Do you want to enter ?", True, BLACK), (295, 460))
            # Show the options
            # Yes
            self.screen.blit(self.warper_font.render("Yes : Press F", True, BLACK), (340, 490))
            # No
            self.screen.blit(self.warper_font.render("No : Press X", True, BLACK), (340, 520))

        #########
        # DEBUG #
        #########
        # Obstacles
        # Show walls
        for wall in self.walls:
            wall.show_wall()
        # HITBOXES
        # Show player hitbox
        pygame.draw.rect(self.screen, (255, 0, 0), self.camera.apply_rect(self.player.hitbox), 2)

        # Update the window
        pygame.display.update()


    # POPUP
    # Warper
    def warper_popup_event(self):
        """
            Manage the inputs during the warper popup
        """

        # Process inputs
        for event in pygame.event.get():
            # Quit the game
            self.quit_game(event)
            if event.type == KEYUP:
                if event.key == pygame.K_f:
                    self.player.current_map = self.current_warper
                    self.warper_popup_flag = False
                elif event.key == pygame.K_x:
                    self.warper_popup_flag = False


    def update(self):
        """
            Update the rects / pos / everything
        """

        self.player.update()
        self.camera.update(self.player)


    def login_screen(self):
        """
            Create the login object
        """

        # Init the login status
        self.login_flag = True
        # Create the login
        self.login = Login(self)


    def load_cfg(self):
        """
            Load the config .json file
        """

        try:
            with open("cfg/cfg.json", "r") as config_file:
                self.cfg = json.loads(config_file.read())
            print("\nConfig loaded.")
        except FileNotFoundError:
            print("\nERROR: cfg.json not found.")
            self.load_cfg_error = True


    def save_cfg(self):
        """
            Save the config file ina .json
        """

        try:
            with open("cfg/cfg.json", "w") as config_file:
                config_file.write(json.dumps(self.cfg, indent= 4))
            print("\nConfig saved.")
        except FileNotFoundError:
            print("\nERROR: cfg.json not found.")


    def image_preloader(self):
        # Image preload
        # Warper
        self.warper_popup_img = pygame.image.load("img/popup/warper/warper_img.png").convert_alpha()


    def quit_game(self, event):
        """
            Manage quit game inputs
        """

        # Let's you quit the game
        if event.type == pygame.QUIT:
            self.playing = False
            self.running = False
            self.save_cfg()
            pygame.quit()


    def launch_game(self):
        """
            Launch a new game | Create the map, the camera, the player
        """

        # Load the Maps
        Map.map_loader(self)
        # Manage the sprites
        # Create the sprites groups
        self.walls = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.warpers = pygame.sprite.Group()
        # generate our player for new party
        for tile_object in self.maps["worldmap"]["map"].tmxdata.objects:
            # Spawn the player
            if tile_object.name == "player":
                self.player = Player(tile_object.x, tile_object.y, "img/avatar/1/", self)
                self.all_sprites.add(self.player)
            # Spawn the walls
            if tile_object.name == "wall":
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.walls.add(Wall(rect, self))
            # Spawn the warpers
            if "warper" in tile_object.name:
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                # Create a temp warper
                temp_warper = Warper(rect, self)
                # Add the name
                setattr(temp_warper, "name", tile_object.name.split("_")[0])
                # Save the warper in the sprite group
                self.warpers.add(temp_warper)

        #########
        # DEBUG #
        #########
        # print(self.walls)
        # print(self.all_sprites)
        # print(self.warpers)
        for warper in self.warpers:
            print(warper.name)

        # Create the camera
        # NEEDS TO BE DELETED AND RECREATED AFTER EACH MAP to NEWMAP TELEPORT
        self.camera = Camera(self.maps["worldmap"]["rect"].width, self.maps["worldmap"]["rect"].height)

        # Set the worldmap flag to true
        # self.worldmap_flag = True
