# coding: utf-8

# additional code
import game.harvest_game.variables_harvest as var

class User_player():
    """
        manages the player class
    """

    def __init__(self, properties_player):
        """
            is the constructor
        """

        # player id in database
        self.id = properties_player[0]
        # name of the player
        self.name = properties_player[1] 
        # velocity of the player
        self.velocity = properties_player[2] 
        # the map number where is the player
        self.id_map = properties_player[3] 
        # the level of the player
        self.id_gamelevel = properties_player[4] 
        # the link to load the seed image
        self.link = properties_player[5]
        # position x of the player on screen
        self.x = properties_player[6] 
        # position y of the player on screen
        self.y = properties_player[7] 
        # check if the seed image has to be show on screen
        self.visible = properties_player[8] 
        # the previous position x, at start is x
        self.previousx = self.x
        # the previous position y, at start is y
        self.previousy = self.y


    def move_up(self, id, y_item):
        """
            moves higher the item on screen
        """

        for player in var.players :
            if id == self.id:
                print("\n le joueur monte\n")
                # save the previous position of the item
                # self.previousy = y_item
                # print(f'Ancienne position de y = celle fournie:: {y_item}')
                # # the item moves hight dependant on his velocity
                self.y = y_item - self.velocity
                print(f'\nNouvelle position y du joueur :: {self.y}')
                # show the item with the new position i player is visible




    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.id} :: {self.name} - visible :: {self.visible}"



# if __name__ == "__main__":
#     pass
