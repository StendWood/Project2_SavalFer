# coding: utf-8

# # additional code
#     # utilities
# # from database_utilities import Database
# from pygame_utilities import Pygame_util

    # global variables
import variables_harvest as var

class Seed():
    """
        Model for seed table in database "P2"
    """

    def __init__(self, properties_seed):
        # seed id in database
        self.id = properties_seed[0]
        # name of the seed
        self.name = properties_seed[1]
        # quantity in stock
        self.quantity = properties_seed[2]
        # period when the seed could be planted
        self.seed_period = properties_seed[3]
        # the name of the product will be pick-up
        self.id_producttosale = properties_seed[4]
        # check if the seed has grown
        self.grown = properties_seed[5]
        # check if the seed image has to be show on screen
        self.visible = properties_seed[6]
        # the link to load the seed image
        self.link = properties_seed[7]
        # position x of the seed on screen
        self.x = properties_seed[8]
        # position y of the seed on screen
        self.y = properties_seed[9]
        # position of seed rect
        # self.position = self.get_rect()
    

    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.id} :: {self.name} - Quantité :: {self.quantity} - Visible :: {self.visible} - Lien :: {self.link}"

    # def to_grow(self):
    #     self.grown = True

    @staticmethod
    def get_visible(id_object):
        """
            put true to the attibut visible (for seed)
        """
        # print(id_object)
        # seed is visible
        for seed in var.seeds:
            if seed.id == id_object:
                seed.visible = True    



        # # show the background of the interface
        # Pygame_util.manage_image(var.window_game, "assets/img/inventory/bg.png", 20, 20)

        # for seed in var.seeds:
        #     if id == seed.id:
        #         # show the seed the player has in his inventory
        #         Pygame_util.manage_image(var.window_game, self.link, 100, 100)





    #     # if the player presses on button left of the mouse
    #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     # si clic sur la souris
    #         # if the place where he pressed is in the surface of the username rectangle
    #         if username_rect.collidepoint(event.pos):  
    #             # the player could tape the username but not the password
    #             username_status = True
    #             password_status = False
    #         # if the place where he pressed is in the surface of the password rectangle
    #         elif password_rect.collidepoint(event.pos):
    #             # the player could tape the password but not the username
    #             password_status = True
    #             username_status = False



if __name__ == "__main__":
    pumpkin.choose_seed(4)
#     seeds=[]
#     seed_1 = Seed(2, "berry", 3, 6)
#     seeds.append(seed_1)
#     seed_2 = Seed(3, "apple", 5, 10)
#     seeds.append(seed_2)
#     seeds.append(Seed(5, "banana", 5, 10))
    
#     print("\nListe des graines :: ")
#     for item in seeds:
#         print(f"{item.name} : {item.quantity} - {item.grown}")
#     banana = [my_seed for my_seed in seeds if my_seed.name == "banana"][0]
#     print("\nLa banane pousse...\n")
#     banana.to_grow()

#     print("Quelle graine a poussé ?")
#     for item in seeds:
#         print(f"- {item.name} : {item.quantity} → {item.grown}")
