# coding: utf-8

# modules
import requests
import json
import pygame
from pprint import pprint

# global variables
import game.harvest_game.variables_harvest as var

# additional code
from game.harvest_game.tkinter_utilities import Tkinter_util
import game.harvest_game.iu_win_lost
from game.harvest_game.iu_flower import Iu_flower


class Flower():
    """
        manage the API test with image of flower
    """

    def __init__(self, name, image_path):
        """
            Constructor of flower object to check in API plantnet
        """
        self.name = name
        self.image_path = image_path
        self.image_data = open(self.image_path, 'rb')
        self.data = {'organs': ['flower']}
        self.files = [('images', (self.image_path, self.image_data))]


    def request_api(self):
        """
            connect to the API database
            get the response
            transform the result in json
            print the result
        """

        req = requests.Request('POST', url=var.api_endpoint, files=self.files, data=self.data)  
        prepared = req.prepare()

        s = requests.Session()
        response = s.send(prepared)

        json_result = json.loads(response.text)

        name_api = (((json_result.get('results'))[0]).get('species')).get('scientificNameWithoutAuthor')
        pourcentage = round(((json_result.get('results'))[0]).get('score')*100)
        print(f'\nIl y a {pourcentage} % de chance pour que cela soit {name_api}.')
        if name_api == "Etlingera elatior":
            # var.good_flower = True
            print("\nTu détiens l'Etlingera elatior ! Mets-la à l'abris sous l'océan !")
            game.harvest_game.iu_win_lost.iu_winner()
        else:
            game.harvest_game.iu_win_lost.iu_looser()


        # @staticmethod
        # def check_flower(name_key_tiled):
        #     """
        #         checks if the current flower is the good one
        #     """

        #     for flower in var.flowers_objects:
        #         if name_check == flower.name:                    
        #             flower.request_api(var.api_endpoint)



    def show_flower_interface(self):
        """
            show the interface for check if the flower is the good one
        """

        var.tkinter = Iu_flower(link=self.image_path)
        var.tkinter.launch_loop()



# if __name__ == "__main__":

#     # for key in var.flowers_dict:
#     #     name = var.flowers_dict[key]["name"]
#     #     image_path = var.flowers_dict[key]["image_path"]
#     #     var.flowers_objects.append(Flower(name, image_path))
#     for flower in var.flowers_objects:

#         flower.request_api(var.api_endpoint)
