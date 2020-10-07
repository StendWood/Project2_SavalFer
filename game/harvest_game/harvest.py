# coding: utf-8

import pygame
import pytmx

import variables_harvest as var

# import
from connect_db import Database
from seed import Seed
from pygame_utilities import Pygame_util
from map_tiled import Map_tiled
from player_harvest import Player_harvest
from touch_function import Touch_function


import psycopg2



def main_harvest(running=True):
    """
        Starts the harvest game
    """
    
    # ** instancier la classe Database
    db = Database()

    # gets the seeds from the database
    seeds_db = db.execute_query(f"SELECT * FROM seed", True)

    # ** instancier la classe Seed
    var.seeds = []

    # seed_1 = Seed(1, 'berry', 3, 6, 1)
    for item in seeds_db:
        var.seeds.append(Seed(item))

    # ** debug *************
    for seed in var.seeds:
        if seed.id == 4   :
            print()
            print(seed.visible)
    print()
    # ********************** 


    # ** launch the game user interface 
    ## generate the window of the game
    window_game = Pygame_util.generate_window("Name", 800, 600)

    ## load tiled map 
    Map_tiled.render(window_game,'assets/maps/HarvestLand/HarvestLand.tmx')
    
    ## update the window with the map
    Pygame_util.update_window()

    ## import player image
    alien = Pygame_util.import_image('assets/img/avatar/alien/alien_purple.png')

    ## show player  on a specific place on screen
    Pygame_util.show_image(window_game, alien, 300, 400 )
    
    ## update the window with the player
    Pygame_util.update_window()

    ## get what the player does
    print()
    print(f' var.touch_key au début :: {var.touch_key}')

    var.touch_key = Pygame_util.get_event()
    
    # var.touch_key = "K_SPACE"
    # ! print()
    print(f" le nom de la touche :: {var.touch_key}")
    print(f" le numéro de la graine :: {var.nb_seed}")
    print()
    
    # {var.touch_functions[key](var.nb_seed) for key in var.touch_functions if key == var.touch_key}
    #* ci_dessus compréhension de dico = ci-dessous
    for key in var.touch_functions:
        print(f" la clé en cours :: {key}")
        if key == var.touch_key :
            var.touch_functions[key](4)

    #* ############################################
    
    # for seed in var.seeds:
    #     if seed.id == 4   :
            #seed.
    # (var.touch_functions.value for key in var.touch_functions if key == touch_key)
    # print(f' visible ou pas :: {visible}')
    print()
    print("A C T I O N")
    print()
    # print()
    # print(f" var.visible_pumpkin :: {var.visible_pumpkin}")
    # print()
    
    #! pumpkin = db.execute_query(f""" SELECT link FROM seed WHERE id=4""")
    ## update the database if visible now and print the pumpkin if it is visible
    for seed in var.seeds:
        if seed.visible == True :
            # update the database with new attribut
            db.execute_query(f"UPDATE seed SET visible = True WHERE id = {seed.id}")
            var.link = seed.link
            # # update the collection ! à suppr si je modifie directement la collection
            # for seed in var.seeds:
            #     if seed.id == 4:
            #         seed.visible = var.visible_pumpkin
            #? debug ####################
            # for seed in var.seeds:
            #     if seed.id == 4:
            #         print()
            #         print(f'visible dans la collection :: {seed.visible}')
            #         print()
            # pumpkin_visible = db.execute_query(f"SELECT seed.visible FROM seed WHERE id = 4", True)
            # print()
            # print(f'pumpkin visible de la bdd : {pumpkin_visible}')
            # print()
            #? ############################## 
        

        # for seed in var.seeds:
        #     if seed.id == 4:
        #         var.link = seed.link

            # show a pumpkin on screen
            # import pumpkin image
            pumpkin = Pygame_util.import_image(var.link)
            
            # show pumpkin on a specific place on screen
            Pygame_util.show_image(window_game, pumpkin, 70, 30 )

            ## update the window with the pumpkin
            Pygame_util.update_window()
                



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