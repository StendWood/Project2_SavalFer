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
The basic main loop, manage the login and the game call.

1. Init the game class
2. Load the config file (.py for now, JSON later)
3. Launch the login loop
4. Check for a username/password match in the database. (The password is hashed using pbkdf2_hmac with 100000 iterations)
5. Launch the pygame loop after a successfull login


### Game
Manage every aspect of the game, game loop, player, obstacles, pnjs, warpers...

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

  ```
   - Set the FPS using the Clock object from pygame
   - Manage the players inputs with .worldmap_event() and .popup_event() methods.
   - Update the game display (player position, sprite animations...) 
   - Draw on the display surface using .draw() method
  ```

### Map
Manage the maps (loading, changing...)
1. The game starts by calling the @staticmethod Map.loader()

    ```python
    # Add to the Game.maps dict every map (here example is with the worldmap
    # Create a Map instance using a .tmx file (see Tiled)
    game.maps["worldmap"]["map"] = Map("assets/maps/world_map/world_map.tmx", game)
        # We use the Game instance to give access to the game attributes.
        # The Map class __init__ call the pytmx.load_pygame(filename) method with load the .tmx file.

    # Create another Map instance for the foreground (will be blited after the player)
    game.maps["worldmap"]["foreground"] = Map("assets/maps/world_map/world_map_foreground.tmx", game)

    # Create the map surface using the .make_map() method
    game.maps["worldmap"]["img"] = game.maps["worldmap"]["map"].make()
        # The .make() method call the .render() method, wich take a surface and draw on it,
        # by unpacking the .tmx file from the Map instance we can draw every layer and create the visual.

    # Create a pygame Rect using the .get_rect() method
    game.maps["worldmap"]["rect"] = game.maps["worldmap"]["img"].get_rect()

    # Load the image for the loading screen when the player teleport to this map.
    game.maps["worldmap"]["loading"] = pygame.image.load("assets/img/login/login_bg.jpg")
    ```

2. The map change is operated by the .transition() method.

    ```python
    # Blit the loading screen using the "loading" key
   self.game.screen.blit(self.game.maps[map_name]["loading"], (0, 0))
    # Empty every Sprites Group
    .empty()
    # Create the current map objects using the .create_map_objects() method
    if self.game.player.current_map != "worldmap":
            # The player is teleporting to a new map wich is not the worldmap
            # We do not use the old_pos or the create_player arguments because the player is already created.
            # We instead use the move_player argument to change the player position where the level starts
            self.create_map_objects(map_name)
        else:
            # The player is teleporting back to the worldmap, we then need to use his old_pos
            # Wich correspond to his position on the worldmap before the teleport.
            self.create_map_objects(map_name, old_pos=True)
    ```
### Sprites
The Sprites class is a parent class to player and pnj.

1. load_animation() : return a list of the different sprites used to animate depending on a list of durations, an image path.
    ```python
    # Save the returned list to the "run_up" dict key
    self.animation_database["run_up"] = self.load_animation(
    #                                 |EACH FRAME STAYS FOR 13 SEC
            f"{self.img_path}run_up", [13, 13, 13, 13, 13, 13, 13, 13, 13], self.frame, self.animations_frames)
    #        |IMG PATH
    ```
2. change_action() : Change the current frame to 0 and change the action attributes if the new action is different from the current action.

3. collision_checker() : check if the sprite is in collision with a any wall.

4. debug_show_rect() : show a red box around the sprite. (Debug purpose only)

### Player
The Player class wich manage every aspect of the player (animations, stats, inventory...).

1. 


## License
[GNU General Public License v3.0](https://raw.githubusercontent.com/StendWood/Project2_SavalFer/master/LICENSE)
