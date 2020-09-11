# coding: utf-8

# Imports
import pygame
import json

# Additional code
from game.config import *
from game.login import Login
from player import Player

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

        # generate our player for new party
        self.player = Player()
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
        
        # check if the player want to go to the right
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width() :   
            self.player.move_right() 
        # check if the player want to go to the left
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0: 
            self.player.move_left()  
        # check if the player want to go up
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:  
            self.player.move_up() 
        # check if the player want to go down
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height():   
            self.player.move_down()  
        # check if the player want to jump
        elif self.pressed.get(pygame.K_SPACE) and self.player.rect.y > 0 :
            self.player.jump()  

    def update(self):
        """
            Update the rects / screen / stuff
        """
        
        # show the player
        screen.blit(self.player.image, self.player.rect)



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
