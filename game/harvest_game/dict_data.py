# coding: utf-8

# additional code:
import variables_harvest as var
from player_harvest import User_player
#     # utilities
import tkinter_utilities
# from database_utilities import Database
# from pygame_utilities import Pygame_util

class Dict_data():
    """
        manages data in dictionnary
    """

    @staticmethod
    def put_function_in_dict_touch_functions():
        """
            puts function as value in the dictionnary touch_function in variables_harvest
        """

        for key in var.touch_functions:
            if key == "K_SPACE":
                var.touch_functions[key] = tkinter_utilities.tkinter_util
            elif key == "K_UP":
                var.touch_functions[key] = User_player.move_up