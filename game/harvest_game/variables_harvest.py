#coding: utf-8

import TEST
from touch_function import Touch_function

# additional code:
# from touch_function import Touch_function

running = True

# info about the window of the game
window_game_choosen = {"width_x" : 1000, "height_y" : 300}

players = []
pressed = {}
# visible_pumpkin = False
link = ""
seeds = []
touch_key = ()
touch_id =""
nb_seed =""


touch_functions = {
    # if space key is touch, show the specified image on screen
    "K_SPACE" : Touch_function.get_visible,
    "" : ""
}

