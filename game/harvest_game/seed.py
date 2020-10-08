# coding: utf-8



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
    

    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.id} :: {self.name} - Quantité :: {self.quantity} - Visible :: {self.visible} - Lien :: {self.link}"

    # def to_grow(self):
    #     self.grown = True



# if __name__ == "__main__":
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
