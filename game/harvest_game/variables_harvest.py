#coding: utf-8

# additional code
from touch_function import Touch_function

# check if the game is finish (False if so)
running = True

# info about the window of the game
window_game_choosen = {"width_x" : 800, "height_y" : 600}

# collections from the database
players = []
seeds = []

# key → value = touch_pressed → functions/game actions
touch_functions = {
    # if space key is touch, show the specified image on screen
    "K_SPACE" : Touch_function.get_visible,
    "" : ""
}

# which seed is planted (= seed.id)
nb_seed =""

# which touch is pressed
pressed = {}




