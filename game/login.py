# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *


class Login:
    """
        Let the player connect to the game
    """

    def __init__(self, game):
        # Init game
        self.game = game
        # Load the background image
        self.bg_image = pygame.image.load("img/login/login_bg.jpg").convert()
        # Load the connexion fields
        self.fields_bg_image = pygame.transform.scale(pygame.image.load("img/login/login_field_bg.png").convert_alpha(), (425, 400))
        # Load fields image
        # Standard
        self.username_image = pygame.transform.scale(pygame.image.load("img/login/field_off.png").convert_alpha(), (210, 50))
        self.password_image = pygame.transform.scale(pygame.image.load("img/login/field_off.png").convert_alpha(), (250, 50))
        # clicked
        self.username_image_on = pygame.transform.scale(pygame.image.load("img/login/field_on.png").convert_alpha(), (210, 50))
        self.password_image_on = pygame.transform.scale(pygame.image.load("img/login/field_on.png").convert_alpha(), (250, 50))

        # Username variables
        self.username_text = ""
        # Init the username status
        self.username_status = False
        # Create the username field rect
        self.username_rect = pygame.Rect(USERNAME_RECT)

        # Password variables
        self.password_text = ""
        self.password_text_placeholder = ""
        # Init the password status
        self.password_status = False
        # Create the password field rect
        self.password_rect = pygame.Rect(PASSWORD_RECT)


        # Validate button
        self.validate_button_off = pygame.transform.scale(pygame.image.load("img/login/validate_button_off.png").convert_alpha(), (200,100))
        self.validate_button_on = pygame.transform.scale(pygame.image.load("img/login/validate_button_on.png").convert_alpha(), (200,100))
        # Validation button mouse hover status
        self.validate_hover = False


    def show_login_screen(self):
        """
            Show and refresh inputs fields
        """

        # Show the login background
        self.game.screen.blit(self.bg_image, LOGIN_BG_POS)
        # Show the fields background
        self.game.screen.blit(self.fields_bg_image, (self.game.screen.get_width() / 4.2, self.game.screen.get_height() / 4))
        # Show the fields depending on click status
        if self.password_status:
            # Display password ON and username OFF
            self.game.screen.blit(self.password_image_on, (PASSWORD_FIELD_RECT))
            self.game.screen.blit(self.username_image, (self.username_rect))
        elif self.username_status:
            # Display password OFF and username ON
            self.game.screen.blit(self.password_image, (PASSWORD_FIELD_RECT))
            self.game.screen.blit(self.username_image_on, (self.username_rect))
        else:
            # display password and username OFF
            self.game.screen.blit(self.password_image, (PASSWORD_FIELD_RECT))
            self.game.screen.blit(self.username_image, (self.username_rect))

        # Validate button hover
        if self.validate_hover:
            # Mouse is on the button
            self.game.screen.blit(self.validate_button_on, VALIDATE_POS)
        else:
            # Mouse is not on the button
            self.game.screen.blit(self.validate_button_off, VALIDATE_POS)
        # Validate button text
        self.validate_button_text = self.game.username_font.render(VALIDATE_TEXT, True, WHITE)
        self.game.screen.blit(self.validate_button_text, (VALIDATE_TEXT_POS))
        # Username
        # Create the username label
        self.username_title = self.game.login_field_title_font.render("Username :", True, BLACK)
        # Create a surface to write the login_text
        self.username_surface = self.game.username_font.render(self.username_text, True, WHITE)
        # Print the login_text in the middle of the surface
        self.game.screen.blit(self.username_surface, (self.username_rect.x+45, self.username_rect.y+5))
        # Print the username title | Position depends on the fields rects
        self.game.screen.blit(self.username_title, (self.username_rect.x+35, self.username_rect.y-50))

        # Password
        self.password_title = self.game.login_field_title_font.render("Password :", True, BLACK)
        self.password_surface = self.game.password_font.render(self.password_text_placeholder, True, WHITE)
        self.game.screen.blit(self.password_surface, (self.password_rect.x, self.password_rect.y+10))
        self.game.screen.blit(self.password_title, (self.password_rect.x+35, self.password_rect.y-50))

        # Refresh the screen
        pygame.display.update()
    
    def login_input(self):
        """
            Manage player input in the login screen
        """

        for event in pygame.event.get():
            # If the player presses on button left of the mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     # si clic sur la souris
                # If the place where he pressed is in the surface of the username rectangle
                if self.username_rect.collidepoint(event.pos):  
                    # The player could tape the username but not the password
                    self.username_status = True
                    self.password_status = False
                # If the place where he pressed is in the surface of the password rectangle
                elif self.password_rect.collidepoint(event.pos):
                    # The player could tape the password but not the username
                    self.password_status = True
                    self.username_status = False

            # If the player could tape in username rect
            if self.username_status == True:
                # If he presses on the key of his keypad
                if event.type == pygame.KEYDOWN:
                    # If he wants to delete the last letter
                    if event.key == pygame.K_BACKSPACE:
                        # Delete the last letter in the string
                        self.username_text = self.username_text[:-1]      
                    else:
                        if len(self.username_text) < USERNAME_LENGTH:
                            # Add the letter pressed
                            self.username_text += event.unicode

            # If the player could tape in password rect
            if self.password_status == True :
                # If he presses on the key of his keypad
                if event.type == pygame.KEYDOWN:
                    # If he wants to delete the last letter
                    if event.key == pygame.K_BACKSPACE:
                        # Delete the last letter in the string
                        self.password_text = self.password_text[:-1]
                        self.password_text_placeholder = self.password_text_placeholder[:-1]
                    else:
                        # Add the letter pressed
                        if len(self.password_text) < PASSWORD_LENGTH:
                            self.password_text += event.unicode
                            self.password_text_placeholder += "*"
                            print(self.password_text)
            
            if self.validate_button_off.get_rect(x=VALIDATE_POS[0], y=VALIDATE_POS[1]).collidepoint(pygame.mouse.get_pos()):
                self.validate_hover = True
            else:
                self.validate_hover = False

            # Let's you quit the game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
