# coding: utf-8

# imports
import pygame
import pytmx

from seed import Seed

# additional code:
# from touch_function import Touch_function
import variables_harvest as var
from connect_db import Database


# FPS = 60    # to define how many frames we update per second
# clock = pygame.time.Clock(FPS)  # to have fixed speed


class Pygame_util():
    """
        manages pygame modules and utilities
    """

    @staticmethod
    def generate_window(window_name, window_width = 800, window_height = 600):
        """
            generates the window of the game
        """

        pygame.display.set_caption(window_name) 
        window_screen = pygame.display.set_mode((window_width, window_height))  

        return window_screen

    @staticmethod
    def import_image(image_link):
        """
            imports an image
        """
    
        imported_image = pygame.image.load(image_link)
        return imported_image


    @staticmethod
    def show_image(screen: pygame.Surface, image, image_place_width = 0, image_place_height = 0 ):
        """
            shows an image on a specific place on window
        """
        screen.blit(image, (image_place_width, image_place_height))

    @staticmethod
    def update_window():
        """
            updates the window
        """
        pygame.display.flip()

    @staticmethod
    def get_event():   #! seed.id   à ajouter et remplacer 4 !
        for event in pygame.event.get(): 
        # check if the event is " close the window"
            if event.type == pygame.QUIT:
                var.running = False
                # ! remettre les données comme au début #############################
                db = Database()
                pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)
                print()
                print(f'pumpkin visible de la bdd avant remise à zéro : {pumpkin_visible}')
                print()
                # update the database with visible is False
                db.execute_query("UPDATE seed SET visible = False WHERE id = 4")
                # check if info "False" is back in DB
                pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)
                print()
                print(f'pumpkin visible de la bdd après remise à zéro : {pumpkin_visible}')
                print()
                # ! à supprimer ######################################################
                pygame.quit()  
                print("\nLa fenêtre est fermée !\n")
                # check if info "False" is back in DB
                pumpkin_visible = db.execute_query(f"SELECT name, visible FROM seed WHERE id = 4", True)
                db.close()
                print()
                print(f'pumpkin visible de la bdd après quitter : {pumpkin_visible}')
                print()
                var.touch_key =()
                return 

            if event.type == pygame.KEYDOWN:
                var.pressed[event.key] = True
                # if space was pressed
                if event.key == pygame.K_SPACE:
                    print("\n space was pressed!\n")
                    print(f'event.key ::{event.key}')
                    var.nb_seed = input("Numéro de la graine :")
                    return (f'K_SPACE')

            

                    # # seed is visible
                    # for seed in var.seeds:
                    #     if seed.id == 4:
                    #         seed.visible = True
                    #         print(f'seed id :: {seed.id}')

                    # exec(f'var.{current_vegetable} = True')

                    # print()
                    # print(f" après avoir appuyer sur espace :: {var.visible_pumpkin}")
                    # print()
            var.touch_key =()
            return 



# if __name__ == "__maim__":
#     pass


# ! ----------------------------------------------------------------------------

    # # show the text on screen
    # username_text = ""
    # # add the letter pressed
    # username_text += event.unicode 


