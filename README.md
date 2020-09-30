# Project 2 : SavalFer

This is our Projet 2 from "Developpeur Web et Web mobile" with ViaFormation

## Technologies

- Python
- PostgreSQL
- Tiled

## Modules

Modules used in the entire project.

- Pygame
- Pytmx
- Psycopg2
- Hashlib

## Usage

Explain how the game works and how to use every class to modify or add new maps, sprites, functionality...

### Global game loop

Main
- Init the game class
- Load the config file (.py for now, JSON later)
- Launch the login loop
- Check for a username/password match in the database. (The password is hashed using pbkdf2_hmac with 100000 iterations)
- Launch the pygame loop after a successfull login

Game
- Load the maps (.tmx files)
- Create the sprites groups for each interactive classes (warpers, pnj, wall...)
- Populate every sprite groups with class instance
```python
# Exemple when loading the worldmap
#                            |CALL THE MAP CLASS METHOD           |MOVE THE PLAYER
self.maps["worldmap"]["map"].create_map_objects("worldmap", True, False)
#        |MAP NAME   |ACCESS THE MAP OBJECT     |MAP NAME   |CREATE THE PLAYER
```

## License
[GNU General Public License v3.0](https://raw.githubusercontent.com/StendWood/Project2_SavalFer/master/LICENSE)
