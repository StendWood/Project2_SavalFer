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
    for seed in seeds_db:
        var.seeds.append(Seed(seed))
    
    # ** instantiate class Player
    # gets the players from the database
    players_db = db.execute_query(f"SELECT * FROM userplayer", True)
    # save the datas in players collection
    for player in players_db:
        var.players.append(User_player(player))


    # ** launch the game user interface 
    ## generate the window of the game
    window_game = Pygame_util.generate_window("Name", var.window_game_choosen["width_x"], var.window_game_choosen["height_y"])

    ## load tiled map 
    Pygame_util.manage_image(window_game,'assets/maps/HarvestLand/HarvestLand.tmx', tiled = True)

    ## import player image
    for player in var.players :
        if player.visible:
            Pygame_util.manage_image(window_game, player.link, player.x, player.y) 

    # ** get what the player does
    var.touch_key = Pygame_util.get_event()
    # checks if the player has done something
    if var.touch_key != None :
        # if yes, do what the player want
        {var.touch_functions[key](var.touch_key[1]) for key in var.touch_functions if key == var.touch_key[0]}

    #? ci_dessus compréhension de dico = ci-dessous
        # for key in var.touch_functions:
        #     print(f" la clé en cours :: {key}")
        #     if key == var.touch_key[0] :
        #         var.touch_functions[key](var.touch_key[1])
    #? ############################################
    
    ## update the database if visible now and print the pumpkin if it is visible
    for seed in var.seeds:
        # check if the seed is visible
        if seed.visible == True :
            # update the database with new attribut
            db.execute_query(f"UPDATE seed SET visible = True WHERE id = {seed.id}")
            # show a pumpkin on screen
            Pygame_util.manage_image(window_game, seed.link, seed.x, seed.y)



if __name__ == "__main__":

    while var.running:
        main_harvest()




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