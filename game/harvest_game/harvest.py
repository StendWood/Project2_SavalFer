# coding: utf-8

# # modules
    # graphism
import pygame
import pytmx
    # database
import psycopg2

# # additional code
    # utilities
from database_utilities import Database
from pygame_utilities import Pygame_util
import tkinter_utilities
    # functions for player actions
from touch_function import Touch_function
    # classes from database
from seed import Seed
from player_harvest import User_player
    # global variables
import variables_harvest as var


def main_harvest(running=True):
    """
        Starts the harvest game
    """
    
    # ** instantiate class Database
    db = Database()

    # ** instantiate class Seed
    # gets the seeds from the database
    seeds_db = db.execute_query(f"SELECT * FROM seed", True)
    # save the datas in seeds collection
    var.seeds = [Seed(seed) for seed in seeds_db]
    
    # ** instantiate class Player
    # gets the players from the database
    players_db = db.execute_query(f"SELECT * FROM userplayer", True)
    # save the datas in players collection
    var.players = [User_player(player) for player in players_db]


    # ** launch the game user interface 
    ## generate the window of the game
    var.window_game = Pygame_util.generate_window(var.window_name, var.window_game_choosen["width_x"], var.window_game_choosen["height_y"])

    ## show tiled map 
    Pygame_util.manage_image(var.window_game,'assets/maps/HarvestLand/HarvestLand.tmx', tiled = True)

    ## show player image
    for player in var.players :
        if player.visible == True:
            Pygame_util.manage_image(var.window_game, player.link, player.x, player.y) 

    # ** get what the player wants to do
    # get which touch he pressed
    var.touch_key = Pygame_util.get_event()
    # check if the player has done something
    if var.touch_key != None :
        # if yes, do what the player want before checking if the second value of the tuple is empty
        if var.touch_key[1] != "":
            if var.touch_key[1] == "T":
                {var.touch_functions[key]() for key in var.touch_functions if key == var.touch_key[0]}
            else:
                {var.touch_functions[key](var.touch_key[1]) for key in var.touch_functions if key == var.touch_key[0]}
        # elif var.touch_key[1] != "seed":
        #     # get which touch he has done
        #     var.touch_key = Pygame_util.get_event()
        #     # check if the player clic on mouse
        #     if var.touch_key[1] != "" :
        #         # get the position of the mouse
        #         object_1 = var.touch_key[1]
        #         # get the image position (rect)

        #         # check if hte mouse in over an image of seed
        #         Pygame_util.check_collision(object_1,)
        #         # if yes, plant the seed
        #                         #!seed.choose_seed(var.touch_key[1])
        #                     #! OU {var.touch_functions[key](var.touch_key[1]) for key in var.touch_functions if key == var.touch_key[0]}

        else:
            {var.touch_functions[key](player, 1, player.y) for key in var.touch_functions if key == var.touch_key[0]}

    #? ci_dessus compréhension de dico = ci-dessous
        # for key in var.touch_functions:
        #     print(f" la clé en cours :: {key}")
        #     if key == var.touch_key[0] :
        #         var.touch_functions[key](var.touch_key[1])
    #? ############################################
    
    ## update the database with what is visible now and show it on screen
    for seed in var.seeds:
        # check if the seed is visible
        if seed.visible == True :
            # update the database with new attribut
            db.execute_query(f"UPDATE seed SET visible = True WHERE id = {seed.id}")
            # show a pumpkin on screen
            Pygame_util.manage_image(var.window_game, seed.link, seed.x, seed.y)
    
    for player in var.players :
        if player.visible == True :
            # if player.y != player.previousy:
            # update the database with new attribut
            db.execute_query(f"UPDATE userplayer SET y = {player.y} WHERE id = {player.id}")
            # show the player on screen at the new position
            Pygame_util.manage_image(var.window_game, player.link, player.x, player.y)

    # tkinter_utilities.tkinter_util()

if __name__ == "__main__":

    while var.running:
        main_harvest()
    
        # if the player decides to quit, update the database like at the beginning
        # # ! remettre les données comme au début #############################
        # pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)
        # print()
        # print(f'pumpkin visible de la bdd avant remise à zéro : {pumpkin_visible}')
        # print()
        # # update the database with visible is False
        # db.execute_query("UPDATE seed SET visible = False")
        # # check if info "False" is back in DB
        # pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed ", True)
        # print()
        # print(f'pumpkin visible de la bdd après remise à zéro : {pumpkin_visible}')
        # print()
        # pygame.quit()  
        # print("\nLa fenêtre est fermée !\n")
        # # check if info "False" is back in DB
        # pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)
        # db.close()
        # print()
        # print(f'pumpkin visible de la bdd après quitter : {pumpkin_visible}')
        # print()




        # #? debug update database for pumpkin ####################

        # # update to True # #
        # db = Database()

        # db.execute_query("UPDATE seed SET visible = True WHERE id = 4")

        # # db.execute_query(f"UPDATE seed SET visible = True WHERE id = 4")
        # pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)

        # print()
        # print(f'pumpkin visible de la bdd : {pumpkin_visible}')
        # print()

        # # update to False # #
        # db = Database()

        # connection = psycopg2.connect(host = "localhost",
        # database = "p2",
        # user = "postgres",
        # password = "Formation2020-at")

        # my_cursor = connection.cursor()
        # sql = "UPDATE seed SET visible = False WHERE id = 4"
        # my_cursor.execute(sql)
        # connection.commit()
        # my_cursor.close()

        # # db.execute_query(f"UPDATE seed SET visible = True WHERE id = 4")
        # pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)

        # print()
        # print(f'pumpkin visible de la bdd : {pumpkin_visible}')
        # print()

        # var.running = False
        # #? ############################## 
        



            # if event.type == pygame.KEYUP:
            #     var.pressed[event.key] = False