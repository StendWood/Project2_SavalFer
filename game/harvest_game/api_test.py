# coding: utf-8

import requests
import json
from pprint import pprint

API_KEY = "2a10jDhRQRaCmFNfafXYEIcRN"  # Set you API_KEY here
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

# hibiscus
image_path_1 = "game/harvest_game/img_api/image_1.jpeg"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = "game/harvest_game/img_api/image_2.jpeg"
image_data_2 = open(image_path_2, 'rb')

# citrouille
image_path_3 = "game/harvest_game/img_api/citrouille-fleur.jpg"
image_data_3 = open(image_path_3, 'rb')

image_path_4 = "game/harvest_game/img_api/citrouille-feuille.jpg"
image_data_4 = open(image_path_4, 'rb')

# banana images
image_path_a = "game/harvest_game/img_api/bananes.png"
image_data_a = open(image_path_a, 'rb')

image_path_b = "game/harvest_game/img_api/banane_feuille.png"
image_data_b = open(image_path_b, 'rb')


data = {
    'organs': ['flower', 'leaf']
}

files = [
    ('images', (image_path_a, image_data_a)),
    ('images', (image_path_b, image_data_b))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)  
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)


nom = (((json_result.get('results'))[0]).get('species')).get('commonNames')
print("Noms communs ::")
for index in range(len(nom)) :
    print(f' - {nom[index]}')
print()
pourcentage = round(((json_result.get('results'))[0]).get('score')*100)
print(f'Pourcentage :: {pourcentage} %')