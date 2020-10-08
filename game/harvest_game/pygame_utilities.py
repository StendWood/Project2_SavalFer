# coding: utf-8

# imports
import pygame
import pytmx

from seed import Seed

# additional code:
import variables_harvest as var
from database_utilities import Database
from map_tiled import Map_tiled


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
    def manage_image(screen: pygame.Surface, image_link, image_place_width = 0, image_place_height = 0, tiled = False):
        """
            imports, shows and updates the screen with an image depending on if it is .tmx or another extension file
        """

        #* check if the extension is .tmx
        # if tiled is True means .tmx so use this fonction
        if tiled:
            # so use this fonction
            Map_tiled.render(screen, image_link)
        # if another extension
        else:
            # load the image in pygame
            imported_image = pygame.image.load(image_link)
            # show the image on a specific place on window
            screen.blit(imported_image, (image_place_width, image_place_height))

        # update the window
        pygame.display.flip()



    @staticmethod
    def get_event():
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
                return 

            if event.type == pygame.KEYDOWN:
                var.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                # if space was pressed
                if event.key == pygame.K_SPACE:
                    # ask the player the seed id
                    var.nb_seed = int(input("Numéro de la graine :"))
                    # return the name of the key (to check in the dictionnary) and the seed id
                    return 'K_SPACE', var.nb_seed
                # touch "z" was pressed
                elif event.key == pygame.K_UP:
                    print(f'\nUP was pressed ! \n')
                    # return the name of the key (to check in the dictionnary)
                    return 'K_UP', ""
                
                # Reset key bool to False
                self.pressed[event.key] = False
            

                    # # seed is visible
                    # for seed in var.seeds:
                    #     if seed.id == 4:
                    #         seed.visible = True
                    #         print(f'seed id :: {seed.id}')

                    # exec(f'var.{current_vegetable} = True')

                    # print()
                    # print(f" après avoir appuyer sur espace :: {var.visible_pumpkin}")
                    # print()
            return 



# if __name__ == "__maim__":
#     pass


# ! ----------------------------------------------------------------------------

    # # show the text on screen
    # username_text = ""
    # # add the letter pressed
    # username_text += event.unicode 


