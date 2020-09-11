# coding: utf-8

# imports
import pygame

class Player():
    """
        Player class
    """

    def __init__(self):
        """
            Constructor
        """

        self.health = 100                         # ! = health_player
        self.max_health = 100                         # ! =  max_health_player
        self.velocity = 1                         # ! =  velocity_player
        self.jump_height = 5
        self.jump_velocity = 3
        self.image = pygame.image.load('images/idle_01.png')
        self.rect = self.image.get_rect() 
        self.rect.x = 170
        self.rect.y = 6


    def move_right(self):
        """
            Move the player to the right
        """

        self.rect.x += self.velocity


    def move_left(self):
        """
            Move the player to the left
        """

        self.rect.x -= self.velocity


    def move_up(self):
        """
            Move the player up
        """

        self.rect.y -= self.velocity
    

    def move_down(self):
        """
            Move the player down
        """

        self.rect.y += self.velocity


    def jump(self):
        """
            the player jumps and go forward
        """

        print("\nJUMP\n")
        self.rect.y -= self.jump_height
        self.rect.x += self.jump_velocity


        

