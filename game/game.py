# coding: utf-8

# Imports
from game.water_source import Water_source
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
from game.views.gui import Gui
from game.api import Flower

# global variables
import game.harvest_game.variables_harvest as var


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
        self.show_actions_font = pygame.font.Font(SHOW_ACTIONS_FONT, 25)

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
            "GardenLand" :
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
            "HarvestLand":
                {# Map instance
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
        # Warper intereactions
        self.warper_popup_flag = False
        self.current_warper = None
        # Inventory interactions
        self.inventory_flag = False
        # Pnj interactions
        self.pnj_popup_flag = False
        self.current_pnj_text = None
        self.is_vendor = None
        # Water sources interactions
        self.water_popup_flag = False
        # Actions
        self.actions_text_flag = False
        self.show_messages_queue = []

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
            if not self.warper_popup_flag and not self.pnj_popup_flag and not self.water_popup_flag:
                # Popup is not active
                if self.player.current_map in ["worldmap","EdWorld", "GardenLand", "HarvestLand"]:
                    self.worldmap_event()
            elif self.warper_popup_flag or self.pnj_popup_flag or self.water_popup_flag:
                # Popup is active
                self.popup_event()
            # Update
            self.update()
            # Draw
            self.draw()

    def worldmap_event(self):
        """
            Listen and process normal inputs
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
                # E
                if event.key == pygame.K_e:
                    # Check for any teleport to enter
                    for warper in self.warpers:
                        warper.show_teleport_prompt()
                    for pnj in self.pnj:
                        if pnj.rect.colliderect(self.player.rect):
                            self.current_pnj_text = pnj.talk_to()
                            self.is_vendor = pnj.is_vendor
                    for water in self.water_sources:
                        if water.rect.colliderect(self.player.rect):
                            self.water_popup_flag = True
                            # Player drink
                            self.show_messages_queue.append(Water_source.drink(self))
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
                self.player.frame, self.player.status = self.player.change_action(self.player.status, "idle_up", self.player.frame)
            elif self.player.status == "run_down":
                self.player.frame, self.player.status = self.player.change_action(self.player.status, "idle_down", self.player.frame)
            elif self.player.status == "run_side":
                self.player.frame, self.player.status = self.player.change_action(self.player.status, "idle_side", self.player.frame)

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
        # Pnj
        for pnj in self.pnj:
            if pnj.can_move:
                if pnj.flip:
                    self.screen.blit(pygame.transform.flip(pnj.image, True, False), 
                                    self.camera.apply_rect(pnj.rect))
                else:
                    self.screen.blit(pnj.image, self.camera.apply_rect(pnj.rect))
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
        self.show_popup(
            self.warper_popup_flag, self.warper_popup_img,
            f"Do you want to enter {self.current_warper}?",
            (250, 450), (275, 460), True)
        # Pnj interactions popup
        self.show_popup(
            self.pnj_popup_flag, self.pnj_popup_img,
            self.current_pnj_text,
            (175, 450), (200, 460), False)
        # Water source popup
        self.show_popup(
            self.water_popup_flag, self.warper_popup_img,
            "Do you want to refill your bottle ?",
            (250, 450), (275, 460), True)
        # Actions popup
        self.show_actions()

        # GUI
        Gui.show_gui(self)

        # #########
        # # DEBUG #
        # #########
        # # Obstacles
        # # Show walls
        # for wall in self.walls:
        #     wall.debug_show_wall()
        # for pnj in self.pnj:
        #     pnj.debug_show_rect(self.screen, self.camera, pnj.rect)
        # # # HITBOXES
        # # # Show player hitbox
        # pygame.draw.rect(self.screen, (255, 0, 0), self.camera.apply_rect(self.player.hitbox), 2)

        # Update the window
        pygame.display.update()

    def popup_event(self):
        """
            Manage the inputs during the a popup
        """

        # Process inputs
        for event in pygame.event.get():
            # Quit the game
            self.quit_game(event)
            if event.type == KEYUP:
                if event.key == pygame.K_f:
                    if self.warper_popup_flag:
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
                        # Change the camera
                        if self.camera.width != self.maps[self.player.current_map]["map"].width:
                            self.camera.width = self.maps[self.player.current_map]["map"].width
                        if self.camera.height != self.maps[self.player.current_map]["map"].height:
                            self.camera.height = self.maps[self.player.current_map]["map"].height
                        # Wait
                        time.sleep(1)
                    elif self.water_popup_flag:
                        self.show_messages_queue.append(Water_source.refill(self))
                        self.water_popup_flag = False
                elif event.key == pygame.K_x:
                    # Reset the flag and var
                    if self.warper_popup_flag:
                        self.warper_popup_flag = False
                        self.current_warper = None
                    elif self.pnj_popup_flag:
                        self.pnj_popup_flag = False
                        self.current_pnj_text = None
                    elif self.water_popup_flag:
                        self.water_popup_flag = False

    def show_popup(self, flag : bool, img : str, text : str, img_position : tuple, txt_position : tuple, give_access : bool = False):
        """
            Show a text in a box with inputs
        """

        if flag:
            # Show the popup background
            self.screen.blit(img, img_position)
            # Blit the text
            self.screen.blit(self.warper_font.render(text, True, BLACK), txt_position)
            # Show the options
            # Yes
            if give_access:
                self.screen.blit(self.warper_font.render("Yes : Press F", True, BLACK), (340, 490))
            # No
            self.screen.blit(self.warper_font.render("No : Press X", True, BLACK), (340, 520))

    def show_actions(self):
        """
            Show what happens after a player actions (refill, drink, teleport, etc...)
        """

        if self.actions_text_flag:
            self.screen.blit(self.actions_text_surface, (50, 50))
            # Message was shown for Nseconds
            if pygame.time.get_ticks() - self.last_actions_timestamp > 3000:
                self.actions_text_flag = False
                self.show_messages_queue.pop(0)
        # Check if there is an action text and if the flag is False
        if len(self.show_messages_queue) > 0 and not self.actions_text_flag:
            # Change the flag
            self.actions_text_flag = True
            # Create the surface
            self.actions_text_surface = pygame.Surface((700, 25))
            # Blit the background on the surface
            self.actions_text_surface.blit(self.show_actions_img, (0, 0))
            # Blit the text on the surface
            self.actions_text_surface.blit(self.warper_font.render(self.show_messages_queue[0], True, BLACK), (10, 2))
            # Get the timestamp
            self.last_actions_timestamp = pygame.time.get_ticks()

    def update(self):
        """
            Update the rects / pos / everything
        """

        self.player.update()
        self.pnj.update()
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
        self.warper_popup_img = pygame.image.load("assets/img/popup/warper/warper_img.png").convert_alpha()
        # Popup
        self.pnj_popup_img = pygame.image.load("assets/img/popup/pnj/pnj_img.png").convert_alpha()
        # Actions
        self.show_actions_img = pygame.image.load("assets/img/popup/actions/actions_img.png").convert_alpha()
        # GUI
        Gui.load_gui_image("health", Gui.health_gui_path)
        Gui.load_gui_image("hydration", Gui.hydration_gui_path)
        Gui.load_gui_image("satiety", Gui.satiety_gui_path)

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
        self.pnj = pygame.sprite.Group()
        self.water_sources = pygame.sprite.Group()
        # Generate the player / walls  / warpers
        self.maps["worldmap"]["map"].create_map_objects("worldmap", True, False)

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

        # initialize the Flower class which is used for API
        for key in var.flowers_dict:
            name = var.flowers_dict[key]["name"]
            image_path = var.flowers_dict[key]["image_path"]
            var.flowers_objects.append(Flower(name, image_path))
