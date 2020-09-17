# coding: utf-8

# Imports
import pygame
import json

# Additional code
from game.config import *
from game.login import Login
from game.player import Player
from game.camera import Camera
from game.data.map import Map
from game.obstacles import Wall

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
        # Font init
        pygame.font.init()
        # Sound init
        pygame.mixer.init()
        self.username_font = pygame.font.SysFont(LOGIN_FONT,22)
        self.password_font = pygame.font.SysFont(LOGIN_FONT,16)
        self.login_field_title_font = pygame.font.SysFont(LOGIN_FONT, 30)
        self.validate_button_font = pygame.font.SysFont(VALIDATE_FONT, 25)
        self.login_error_font = pygame.font.SysFont(ERROR_FONT, 15)
        # Create the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Change the window name
        pygame.display.set_caption("SavalFer")
        # Create the clock
        self.clock = pygame.time.Clock()
        self.running = True
        # touch pressed
        self.pressed = {} 


    def run(self):
        """
            Game loop | FPS, Event, Update, 
        """

        # Main loop
        # Set playing to true
        self.playing = True
        while self.playing:
            # Clock the FPS
            self.clock.tick(FPS)
            # Manage inputs
            self.event()
            # Update
            self.update()
            # Draw
            self.draw()


    def event(self):
        """
            Listen and process inputs
        """

        # Process inputs
        for event in pygame.event.get():
            # Let's you quit the game
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                self.save_cfg()
                pygame.quit()
            # get what the player has done
            # detect if the player release a key from the keypad
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            # detect if the key is no more used
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                self.pressed[event.key] = False
        
        # Manage movements inputs
        # check if the player want to go to the right
        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)):
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
            Draw the elements and refresh the screen
        """

        # FPS counter
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # Map
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        # Draw every sprites (Player and monsters)
        for sprite in self.all_sprites:
            if self.player.flip:
                self.screen.blit(pygame.transform.flip(sprite.image, True, False), self.camera.apply_rect(sprite.rect))
            else:
                self.screen.blit(sprite.image, self.camera.apply_rect(sprite.rect))
        # Map foreground
        self.screen.blit(self.map_foreground_img, self.camera.apply_rect(self.map_rect))
        # DEBUG
        # Obstacles
        # Show walls
        for wall in self.walls:
            wall.show_wall()
        # HITBOXES
        # Show player hitbox
        # pygame.draw.rect(self.screen, (255, 0, 0), self.camera.apply_rect(self.player.rect), 2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.camera.apply_rect(self.player.hitbox), 2)

        # update the window
        pygame.display.update()


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


    def launch_game(self):
        """
            Launch a new game | Create the map, the camera, the player
        """

        # Load the world map
        self.map = Map("assets/maps/world_map/world_map.tmx")
        self.map_foreground = Map("assets/maps/world_map/world_map_foreground.tmx")
        # Create the map image
        self.map_img = self.map.make_map()
        self.map_foreground_img = self.map_foreground.make_map()
        # Create the map rect
        self.map_rect = self.map_img.get_rect()
        # Manage the sprites
        i = 0
        self.walls = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        # generate our player for new party
        for tile_object in self.map.tmxdata.objects:
            # Spawn the player
            if tile_object.name == "player":
                self.player = Player(tile_object.x, tile_object.y, "img/avatar/1/", self)
                self.all_sprites.add(self.player)
        # Spawn the walls
            if tile_object.name == "wall":
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                exec(f"self.wall_{i} = Wall(rect, self)")
                eval(f"self.walls.add(self.wall_{i})")
                i += 1
        # Create the camera
        self.camera = Camera(self.map.width, self.map.height)
