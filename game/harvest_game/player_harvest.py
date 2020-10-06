# coding: utf-8

import pygame
import variables_harvest as var


class Player_harvest():
    """
        manages the player class
    """

    def __init__(self, name, image, x, y):
        """
            is the constructor
        """

        # name
        self.name = name 

        # image
        self.image = image

        # position
        self.x = x 
        self.y = y 


    # def get_rect(self, image_link):
    #     """
    #         get he position of the player with a rect
    #     """
    
    #     self.rect = self.image_link.get_rect()
        
    #     x = self.rect.x
    #     y = self.rect.y


# if __name__ == "__main__":
#     var.players = Player_harvest('alien', 'assets/img/avatar/alien/alien purple.png', 100, 100)
#     print(var.players)
#     print(var.players.x)
