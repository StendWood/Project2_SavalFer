#coding: utf-8


# check if the game is finish (False if so)
running = True

# ** datas for Pygame
# info about the window of the game
# the name
window_name = "Harvest Land"
# the size
window_game_choosen = {"width_x" : 800, "height_y" : 600}
# the image
window_game = ""

# ** datas for Tkinter
window_tk = ""
tkinter = []
create_tk = True

# collections from the database
players = []
seeds = []

# key → value = touch_pressed → functions/game actions
touch_functions = {
    # if space key is touch, show the specified image on screen
    "K_SPACE" : "None",
    "K_UP" : "None"
}

# which seed is planted (= seed.id)
nb_seed =""

# which touch is pressed
pressed = {}






