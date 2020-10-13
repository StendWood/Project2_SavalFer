# coding: utf-8

# # additional code:
    # global variables
import variables_harvest as var
#     # utilities
# from database_utilities import Database
# from pygame_utilities import Pygame_util

class Touch_function():
    """
        manages all the functions when a touch is pressed
    """


    @staticmethod
    def get_visible(id_object):
        """
            put true to the attibut visible (for seed)
        """
        # print(id_object)
        # seed is visible
        for seed in var.seeds:
            if seed.id == id_object:
                seed.visible = True
                #! print(f'seed name :: {seed.name} - visible :: {seed.visible}')
        




        
        # ! à supprimer car circular import (pygame_util, touch_fn, var, pygame_util)
        # # update the database with what is visible now and show it on screen
        # for seed in var.seeds:
        #     # check if the seed is visible
        #     if seed.visible == True :
        #         # update the database with new attribut
        #         connexion.execute_query(f"UPDATE seed SET visible = True WHERE id = {seed.id}")
        #         # show a pumpkin on screen
        #         Pygame_util.manage_image(screen, seed.link, seed.x, seed.y)
        # ! 

