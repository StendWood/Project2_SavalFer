#coding: utf-8


# check if the game is finish (False if so)
running = True

# ** datas for Pygame
## info about the window of the game
    # the name
window_name = "Harvest Land"
    # the size
window_game_choosen = {"width_x" : 800, "height_y" : 600}
    # the image
window_game = ""
    # which touch is pressed
pressed = {}

# ** datas for Tkinter
window_tk = ""
tkinter = []
create_tk = True

# ** collections from the database
players = []
seeds = []

# ** dictonnary to manage action
# key → value = touch_pressed → functions/game actions
touch_functions = {
    # if space key is touch, show the specified image on screen
    "K_SPACE" : "None",
    "K_UP" : "None"
}

# ** data to manage the API test
    # connexion
API_KEY = "2a10jDhRQRaCmFNfafXYEIcRN"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"
    # dictionnary to manage the images of flower
flowers_dict = {
    "flower_1" :   {
        "name" : "Etlingera elatior",
        "image_path" : "assets/img/api/99-Etlingera-elatior.png",
        },
    "flower_2" :   {
        "name" : "Aechmea fasciata",
        "image_path" : "assets/img/api/73-Aechmea-fasciata.png",
        },
    "flower_3" :   {
        "name" : "Guzmania lingulata",
        "image_path" : "assets/img/api/23-Guzmania-lingulata.png",
        }
}

flowers_objects = []

frame_flower = None

good_flower = False




# which seed is planted (= seed.id)
nb_seed =""








