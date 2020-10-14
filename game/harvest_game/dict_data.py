# coding: utf-8

# additional code:
import variables_harvest as var
from player_harvest import User_player
#     # utilities
from tkinter_utilities import Tkinter_util


class Dict_data():
    """
        manages data in dictionnary
    """

    @staticmethod
    def put_function_in_dict_touch_functions():
        """
            puts function as value in the dictionnary touch_function in variables_harvest
        """

        var.touch_functions["K_SPACE"] = Tkinter_util
        var.touch_functions["K_UP"] = User_player.move_up