# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *
from game.login import Login

class Game:
    """
        Main game class
    """

    def __init__(self):
        # Pygame init
        pygame.init()
        # Font init
        pygame.font.init()
        self.username_font = pygame.font.SysFont(LOGIN_FONT,25)
        self.password_font = pygame.font.SysFont(LOGIN_FONT,16)
        self.login_field_title_font = pygame.font.SysFont(LOGIN_FONT, 30)
        self.validate_button_font = pygame.font.SysFont(VALIDATE_FONT, 25)
        # Create the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Change the window name
        pygame.display.set_caption("SavalFer")
        # Create the clock
        self.clock = pygame.time.Clock()
        self.running = True


    def run(self):
        """
            Game loop
        """

        # Main loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()


    def event(self):
        """
            Listen and process inputs
        """

        # Process inputs
        for event in pygame.event.get():
            # Let's you quit the game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


    def login_screen(self):
        """
            Create the login object
        """

        # Init the login status
        self.login_flag = True
        # Create the login
        self.login = Login(self)
