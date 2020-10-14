#coding: utf-8

# additional code
from touch_function import Touch_function
from player_harvest import User_player
import tkinter_utilities
# from pygame_utilities import Pygame_util
# from seed import Seed

# check if the game is finish (False if so)
running = True

# info about the window of the game
# the name
window_name = "Harvest Land"
# the size
window_game_choosen = {"width_x" : 800, "height_y" : 600}
# the image
window_game = ""

# collections from the database
players = []
seeds = []

# key → value = touch_pressed → functions/game actions
touch_functions = {
    # if space key is touch, show the specified image on screen
    "K_SPACE" : tkinter_utilities.tkinter_util,
    "K_UP" : User_player.move_up,
    "MOUSEBUTTONDOWN" : "Seed.choose_seed"
}

# which seed is planted (= seed.id)
nb_seed =""

# which touch is pressed
pressed = {}






