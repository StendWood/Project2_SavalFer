# Project 2 : SavalFer

This is our Projet 2 from "Developpeur Web et Web mobile" with ViaFormation

## Technologies

- Python
- PostgreSQL
- Tiled

## Modules

Modules used in the entire project.

![alt text](https://www.pygame.org/images/logo_lofi.png)
- Pytmx
- Psycopg2
- Hashlib

## Usage

Explain how the game works and how to use every class to modify or add new maps, sprites, functionality...


### Main
1. Init the game class
2. Load the config file (.py for now, JSON later)
3. Launch the login loop
4. Check for a username/password match in the database. (The password is hashed using pbkdf2_hmac with 100000 iterations)
5. Launch the pygame loop after a successfull login

### Game
1. Load the maps (.tmx files)
2. Create the sprites groups for each interactive classes (warpers, pnj, wall...)
3. Populate every sprite groups with class instance
```python
# Exemple when loading the worldmap

#                            |CALL THE MAP CLASS METHOD           |MOVE THE PLAYER
self.maps["worldmap"]["map"].create_map_objects("worldmap", True, False)
#        |MAP NAME   |ACCESS THE MAP OBJECT     |MAP NAME   |CREATE THE PLAYER

# There is a last argument named: old_pos (False by default),
# it let's you use the position of the player on the worldmap before a teleport.
```

4. Create the camera using the current map Rect (width and height is changed after every map load to match the current map size.)
```python
#                                         |ACCESS THE RECT OF THE MAP
self.camera = Camera(self.maps["worldmap"]["rect"].width, self.maps["worldmap"]["rect"].height)
#                                                 |GET THE MAP RECT WIDTH              |GET THE MAP RECT HEIGHT
```
5. The main game loop .run()
  ```bash
   - Set the FPS using the Clock object from pygame
   - Manage the players inputs with .worldmap_event() and .popup_event() methods.
   - Update the game display (player position, sprite animations...) 
   - Draw on the display surface using .draw() method
  ```

## License
[GNU General Public License v3.0](https://raw.githubusercontent.com/StendWood/Project2_SavalFer/master/LICENSE)
