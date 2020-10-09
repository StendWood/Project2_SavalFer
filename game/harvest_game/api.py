# coding: utf-8

# imports modules
# import requests


# def Main():
#     """
#         Main function
#     """

#     # variables
#     # MinProductsInCategory = 10  # to filter categories
#     # MaxProductsInCategory = 20  # to filter categories
#     # MaxCategories = 200  # limitation for demo
#     # Categories = []
#     # Products = []

#     # get categories from API
#     print("\nInterrogation de l'API...")
#     Response = requests.get("https://identify.plantnet.org/explo/reunion.json")
#     # Response = requests.get("https://fr.openfoodfacts.org/categories.json")
#     Results = Response.json()



# ! from plantnet 
import requests
import json
from pprint import pprint

API_KEY = "2a10jDhRQRaCmFNfafXYEIcRN"  # Set you API_KEY here
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

image_path_1 = "game/harvest_game/img_api/image_1.jpeg"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = "game/harvest_game/img_api/image_2.jpeg"
image_data_2 = open(image_path_2, 'rb')

data = {
    'organs': ['flower', 'leaf']
}

files = [
    ('images', (image_path_1, image_data_1)),
    ('images', (image_path_2, image_data_2))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)  
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

# pprint(f'\nresponse status_code :: {response.status_code}')
pprint(f'\nresultat en json :: {json_result}')
# print(f'Response, est ce un json :\n    {response.text}')
# ! response.text est un dico

# recherche = response.text.get('query')
#     recherche = response.text.get('query')
# AttributeError: 'str' object has no attribute 'get'

recherche = json_result.get('results')
print(f' recherche sur results :: {recherche}')
recherche_2 = recherche.get('species')
print(f' recherche sur species :: {recherche_2}')