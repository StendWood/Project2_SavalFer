# coding: utf-8

# Imports
from game.data.database import Database
import pygame
import json
import time

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
        # Init the database
        self.db = Database()
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
        self.warper_font = pygame.font.Font(WARPER_FONT, 20)
        self.inventory_font = pygame.font.Font(WARPER_FONT, 18)

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
                    "map" : None,
                    # Map foreground instance
                    "foreground" : None,
                    # Map image
                    "img" : None,
                    # Map foreground image
                    "fg_img" : None,
                    # Map Rect
                    "rect" : None,
                    # Loading BG
                    "loading" : None,
                },
            "EdWorld" :
                {
                    # Map instance
                    "map" : None,
                    # Map foreground instance
                    "foreground" : None,
                    # Map image
                    "img" : None,
                    # Map foreground image
                    "fg_img" : None,
                    # Map Rect
                    "rect" : None,
                    # Loading BG
                    "loading" : None,
                },
        }

        # Flag management
        self.warper_popup_flag = False
        self.inventory_flag = False
        self.current_warper = None


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
                elif self.player.current_map == "EdWorld":
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
                # I
                elif event.key == pygame.K_i:
                    if self.inventory_flag:
                        self.inventory_flag = False
                    else:
                        self.inventory_flag = True
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
        if self.maps[self.player.current_map]["fg_img"] is not None:
            self.screen.blit(self.maps[self.player.current_map]["fg_img"], 
                            self.camera.apply_rect(self.maps[self.player.current_map]["rect"]))

        # INVENTORY
        # Show the player inventory
        if self.inventory_flag:
            # Blit the inventory page background
            self.screen.blit(self.player.inventory.inventory_bg, (50, 50))
            # # Blit the items into the inventory page
            for item in self.player.inventory.items:
                self.screen.blit(item.image, item.rect)
        # Item tooltip on mouseover if inventory is open
        if self.inventory_flag:
            self.player.inventory.item_mouseover()
        # Warper popup for teleport
        if self.warper_popup_flag:
            # Show the popup background
            self.screen.blit(self.warper_popup_img, (250, 450))
            # Blit the text
            self.screen.blit(self.warper_font.render(f"Do you want to enter {self.current_warper}?", True, BLACK), (275, 460))
            # Show the options
            # Yes
            self.screen.blit(self.warper_font.render("Yes : Press F", True, BLACK), (340, 490))
            # No
            self.screen.blit(self.warper_font.render("No : Press X", True, BLACK), (340, 520))

        # #########
        # # DEBUG #
        # #########
        # # Obstacles
        # # Show walls
        # for wall in self.walls:
        #     wall.show_wall()
        # # HITBOXES
        # # Show player hitbox
        # pygame.draw.rect(self.screen, (255, 0, 0), self.camera.apply_rect(self.player.hitbox), 2)

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
                    # Save the old player pos
                    if self.player.current_map == "worldmap":
                        self.player.save_pos()
                    # Change the current map var
                    self.player.current_map = self.current_warper
                    # Reset the current warper
                    self.current_warper = None
                    # Set the warper popup to False
                    self.warper_popup_flag = False
                    # Load the new map objects
                    self.maps[self.player.current_map]["map"].transition(self.player.current_map)
                    # Wait
                    time.sleep(1)
                elif event.key == pygame.K_x:
                    # Reset the flag and var
                    self.warper_popup_flag = False
                    self.current_warper = None


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
        Map.loader(self)
        # Manage the sprites
        # Create the sprites groups
        self.walls = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.warpers = pygame.sprite.Group()
        # Generate the player / walls  / warpers
        self.maps["worldmap"]["map"].create_obstacles_n_warpers("worldmap", True, False)

        #########
        # DEBUG #
        #########
        # print(self.walls)
        # print(self.all_sprites)
        # print(self.warpers)
        # for warper in self.warpers:
        #     print(warper.name)

        # Create the camera
        # NEEDS TO BE DELETED AND RECREATED AFTER EACH MAP to NEWMAP TELEPORT
        self.camera = Camera(self.maps["worldmap"]["rect"].width, self.maps["worldmap"]["rect"].height)

        # Set the worldmap flag to true
        # self.worldmap_flag = True
