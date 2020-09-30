# coding: utf-8

# Imports
import pygame

# Additional code
from game.config import *
from game.data.database import *

class Login:
    """
        Let the player connect to the game
    """

    def __init__(self, game):
        # Init game
        self.game = game
        # Load the background image
        self.bg_image = pygame.image.load("assets/img/login/login_bg.jpg").convert()
        self.game.screen.blit(self.bg_image, LOGIN_BG_POS)
        # Load the connexion fields
        self.fields_bg_image = pygame.transform.scale(pygame.image.load("assets/img/login/login_field_bg.png").convert_alpha(), (425, 400))
        # Load fields image
        # Standard
        self.username_image = pygame.transform.scale(pygame.image.load("assets/img/login/field_off.png").convert_alpha(), (210, 50))
        self.password_image = pygame.transform.scale(pygame.image.load("assets/img/login/field_off.png").convert_alpha(), (250, 50))
        # Glowing
        self.username_image_on = pygame.transform.scale(pygame.image.load("assets/img/login/field_on.png").convert_alpha(), (210, 50))
        self.password_image_on = pygame.transform.scale(pygame.image.load("assets/img/login/field_on.png").convert_alpha(), (250, 50))

        # Username variables
        if self.game.cfg["save_username"]:
            self.username_text = self.game.cfg["username_text"]
        else:
            self.username_text = ""
        # Init the username status
        self.username_status = False
        # Create the username field rect
        self.username_rect = pygame.Rect(USERNAME_RECT)
        # Render username title text
        self.username_title = self.game.login_field_title_font.render(USERNAME_TITLE, True, BLACK)

        # Password variables
        self.password_text = ""
        self.password_text_placeholder = ""
        # Init the password status
        self.password_status = False
        # Create the password field rect
        self.password_rect = pygame.Rect(PASSWORD_RECT)
        # Render password title text
        self.password_title = self.game.login_field_title_font.render(PASSWORD_TITLE, True, BLACK)

        # Save username tickboxes
        self.save_username_text =  self.game.login_error_font.render(SAVE_USERNAME_TEXT, True, BLACK)
        self.save_username_button_off = pygame.transform.scale(pygame.image.load("assets/img/login/save_username_off.png").convert_alpha(), (30, 30))
        self.save_username_button_off_hover = pygame.transform.scale(pygame.image.load("assets/img/login/save_username_off_hover.png").convert_alpha(), (30, 30))
        self.save_username_button_on = pygame.transform.scale(pygame.image.load("assets/img/login/save_username_on.png").convert_alpha(), (30, 30))
        self.save_username_button_on_hover = pygame.transform.scale(pygame.image.load("assets/img/login/save_username_on_hover.png").convert_alpha(), (30, 30))
        self.save_username_hover = False

        # Validate button
        self.validate_button_off = pygame.transform.scale(pygame.image.load("assets/img/login/validate_button_off.png").convert_alpha(), (200,100))
        self.validate_button_on = pygame.transform.scale(pygame.image.load("assets/img/login/validate_button_on.png").convert_alpha(), (200,100))
        # Validation button mouse hover status
        self.validate_hover = False
        # Validate button text
        self.validate_button_text = self.game.username_font.render(VALIDATE_TEXT, True, WHITE)

        # Error images
        self.error_bg = pygame.image.load("assets/img/login/error_bg.png").convert_alpha()
        self.error_button = pygame.image.load("assets/img/login/error_button.png").convert_alpha()
        self.error_text = self.game.login_error_font.render(ERROR_TEXT, True, RED)

        # Create a db object
        self.db = Database(self)
        # Init the login error flag
        self.login_error = False

        # Launch sound
        pygame.mixer.music.load('assets/sounds/cheerful _orchestral.ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)


    def show_login_screen(self):
        """
            Show and refresh inputs fields
        """

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
        # Render validate text
        self.game.screen.blit(self.validate_button_text, (VALIDATE_TEXT_POS))
        # Username
        # Create a surface to write the login_text
        self.username_surface = self.game.username_font.render(self.username_text, True, WHITE)
        # Print the login_text in the middle of the surface
        self.game.screen.blit(self.username_surface, (self.username_rect.x+20, self.username_rect.y+10))
        # Print the username title | Position depends on the fields rects
        self.game.screen.blit(self.username_title, (self.username_rect.x+35, self.username_rect.y-40))

        # Password
        self.password_surface = self.game.password_font.render(self.password_text_placeholder, True, WHITE)
        self.game.screen.blit(self.password_surface, (self.password_rect.x, self.password_rect.y+10))
        self.game.screen.blit(self.password_title, (self.password_rect.x+35, self.password_rect.y-45))

        # Blit save username text
        self.game.screen.blit(self.save_username_text, (SAVE_USERNAME_POS[0]+38, SAVE_USERNAME_POS[1]+7))
        # Manage save username tickboxe states
        if self.save_username_hover and not self.game.cfg["save_username"]:
            # Mousehover and box not ticked
            self.game.screen.blit(self.save_username_button_off_hover, SAVE_USERNAME_POS)
        elif self.save_username_hover and self.game.cfg["save_username"]:
            # Mousehover and box ticked
            self.game.screen.blit(self.save_username_button_on_hover, SAVE_USERNAME_POS)
        elif self.game.cfg["save_username"]:
            # Box ticked
            self.game.screen.blit(self.save_username_button_on, SAVE_USERNAME_POS)
        else:
            self.game.screen.blit(self.save_username_button_off, SAVE_USERNAME_POS)

        # Show the error message when credentials are not found in the DB
        if self.login_error:
            # Blit the error bg
            self.game.screen.blit(self.error_bg, (ERROR_BG_POS[0], ERROR_BG_POS[1]))
            self.game.screen.blit(self.error_button, (ERROR_BUTTON_POS[0], ERROR_BUTTON_POS[1]))
            # Show the error text
            self.game.screen.blit(self.error_text, (ERROR_TEXT_POS[0], ERROR_TEXT_POS[1]))

        # Refresh the screen
        pygame.display.update()


    def login_input(self):
        """
            Manage player input in the login screen
        """

        for event in pygame.event.get():
            # If the player presses on button left of the mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self.login_error:
                    # If the place where he pressed is in the surface of the username rectangle
                    if self.username_rect.collidepoint(event.pos):  
                        # The player can enter the username but not the password
                        self.username_status = True
                        self.password_status = False
                    # If the place where he pressed is in the surface of the password rectangle
                    elif self.password_rect.collidepoint(event.pos):
                        # The player can enter the password but not the username
                        self.password_status = True
                        self.username_status = False
                    # Clicked outside any entry fields
                    elif not self.password_rect.collidepoint(event.pos):
                        self.password_status = False
                        self.username_status = False
                else:
                    # Player clicked on the error close button
                    if self.error_button.get_rect(x=ERROR_BUTTON_POS[0], y=ERROR_BUTTON_POS[1]).collidepoint(event.pos):
                        # Reset the error flag
                        self.login_error = False

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
                            if event.key != pygame.K_TAB and event.key != pygame.K_RETURN:
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
                            if event.key != pygame.K_TAB and event.key != pygame.K_RETURN:
                                self.password_text += event.unicode
                                self.password_text_placeholder += "*"
                                print(self.password_text)

            # Check tab and enter keys
            if event.type == pygame.KEYDOWN:
                # Tabulation key
                if event.key == pygame.K_TAB and not self.login_error:
                    if self.password_status:
                        self.password_status = False
                        self.username_status = True
                    else:
                        self.password_status = True
                        self.username_status = False

                # Enter key only if no connection error is raised
                if event.key == pygame.K_RETURN and not self.login_error:
                    # Reset fields active flag
                    self.password_status = False
                    self.username_status = False
                    # Check if credentials match the DB
                    self.db.password_checker(self.username_text, self.password_text)

            # Check for validate button mousehover
            if self.validate_button_off.get_rect(x=VALIDATE_POS[0], y=VALIDATE_POS[1]).collidepoint(pygame.mouse.get_pos())\
                and not self.login_error:
                self.validate_hover = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check if the player click on the validation button
                    if self.validate_button_on.get_rect(x=VALIDATE_POS[0], y=VALIDATE_POS[1]).collidepoint(event.pos)\
                        or self.validate_button_off.get_rect(x=VALIDATE_POS[0], y=VALIDATE_POS[1]).collidepoint(event.pos):
                        # Check if credentials match the DB
                        self.db.password_checker(self.username_text, self.password_text)
            # Mousehover username save tickbox
            elif self.save_username_button_off.get_rect(x=SAVE_USERNAME_POS[0], y=SAVE_USERNAME_POS[1]).collidepoint(pygame.mouse.get_pos())\
                and not self.login_error:
                # Chang emousehover flag
                self.save_username_hover = True
                # Check for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check if the player click on the remember me button
                    if self.save_username_button_on.get_rect(x=SAVE_USERNAME_POS[0], y=SAVE_USERNAME_POS[1]).collidepoint(event.pos)\
                        and self.game.cfg["save_username"]:
                            self.game.cfg["save_username"] = False
                    else:
                        self.game.cfg["save_username"] = True
            else:
                # Reset the mousehover flags
                self.validate_hover = False
                self.save_username_hover = False

            # Let's you quit the game
            if event.type == pygame.QUIT:
                self.game.runing = False
                self.game.cfg["username_text"] = self.username_text
                self.game.save_cfg()
                pygame.quit()
