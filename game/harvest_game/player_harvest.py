# coding: utf-8

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


    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.id} :: {self.name} - visible :: {self.visible}"

    # def get_rect(self, image_link):
    #     """
    #         get he position of the player with a rect
    #     """
    
    #     self.rect = self.image_link.get_rect()
        
    #     x = self.rect.x
    #     y = self.rect.y


# if __name__ == "__main__":
#     var.players = Player_harvest('alien', 'assets/img/avatar/alien/alien purple.png', 100, 100)
#     print(var.players)
#     print(var.players.x)
