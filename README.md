# Project 2 : SavalFer

This is our Projet 2 from "*Developpeur Web et Web mobile*" with ViaFormation

## Technologies

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Tiled](https://www.mapeditor.org/)

## Modules

Modules used in the entire project.

![alt text](https://www.pygame.org/images/logo_lofi.png)
- [Pygame](https://www.pygame.org/news)
- [Pytmx](https://pytmx.readthedocs.io/en/latest/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Hashlib](https://docs.python.org/3/library/hashlib.html)

## Usage

Explain how the game works and how to use every class to modify or add new maps, sprites, functionality...


### Main
The basic main loop, manage the login and the game call.

1. Init the game class
2. Load the config file (**.py for now, JSON later**)
3. Launch the login loop
4. Check for a username/password match in the database. (**The password is hashed using pbkdf2_hmac with 100000 iterations**)
5. Launch the pygame loop after a successfull login

***
### Game
Manage every aspect of the game, game loop, player, obstacles, pnjs, warpers...

1. Load the maps (**.tmx files**)
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

4. Create the camera using the current map **Rect** (**width** and **height** is changed **after every map load** to match the current map size.)

```python
#                                         |ACCESS THE RECT OF THE MAP
self.camera = Camera(self.maps["worldmap"]["rect"].width, self.maps["worldmap"]["rect"].height)
#                                                 |GET THE MAP RECT WIDTH              |GET THE MAP RECT HEIGHT
```

5. The main game loop *__.run()__*

  ```
   - Set the FPS using the Clock object from pygame
   - Manage the players inputs with .worldmap_event() and .popup_event() methods.
   - Update the game display (player position, sprite animations...) 
   - Draw on the display surface using .draw() method
  ```
***
### Map
Manage the maps (loading, changing...)
1. The game starts by calling the *@staticmethod* *__Map.loader()__*

    ```python
    # Add to the Game.maps dict every map (here example is with the worldmap
    # Create a Map instance using a .tmx file (see Tiled)
    game.maps["worldmap"]["map"] = Map("assets/maps/world_map/world_map.tmx", game)
        # We use the Game instance to give access to the game attributes.
        # The Map class __init__ call the pytmx.load_pygame(filename) method with load the .tmx file.

    # Create another Map instance for the foreground (will be blited after the player)
    game.maps["worldmap"]["foreground"] = Map("assets/maps/world_map/world_map_foreground.tmx", game)

    # Create the map surface using the .make() method
    game.maps["worldmap"]["img"] = game.maps["worldmap"]["map"].make()
        # The .make() method call the .render() method, wich take a surface and draw on it,
        # by unpacking the .tmx file from the Map instance we can draw every layer and create the visual.

    # Create a pygame Rect using the .get_rect() method
    game.maps["worldmap"]["rect"] = game.maps["worldmap"]["img"].get_rect()

    # Load the image for the loading screen when the player teleport to this map.
    game.maps["worldmap"]["loading"] = pygame.image.load("assets/img/login/login_bg.jpg")
    ```

2. The map change is operated by the *__.transition()__* method.

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
***
### Sprites
The Sprites class is a parent class to player and pnj. **(Not te be confused with the pygame.sprite.Sprite class)**

1. *__Sprites.load_animation()__* :

    Return a list of the different sprites used to animate depending on a list of durations, an image path.
    ```python
    # Save the returned list to the "run_up" dict key
    self.animation_database["run_up"] = self.load_animation(
    #                                 |EACH FRAME STAYS FOR 13 SEC
            f"{self.img_path}run_up", [13, 13, 13, 13, 13, 13, 13, 13, 13], self.frame, self.animations_frames)
    #        |IMG PATH
    ```
2. *__Sprites.change_action()__* :

    Change the current frame to 0 and change the action attributes if the new action is different from the current action.

3. *__Sprites.collision_checker()__* :

    Check if the sprite is in collision with a any wall.

4. *__Sprites.debug_show_rect()__* :

    show a red box around the sprite. (Debug purpose only)

***
### Player
The Player class wich manage every aspect of the player (animations, stats, inventory...).

1. 

***
## How to add your Map
**Follow every steps, if any is missing you expose the programm to bugs and whatnot.**
1. Create your map using Tiled (*.tmx file*)

    Make your sure you have an object named *player* and named *worldmap_warper*, to respectively place the player when the map change and to be able to port back to the worldmap.

2. Save every new tilesets in (*.tsx file + .png file*):

      *assets/tilesets/__map_name__*

3. Save your .tmx map file in :

   *assets/maps/__map_name__*

4. Add your map to the map dict in game and in the *@staticmethod* .loader()
    ```python
    # Load the map .tmx file
    game.maps[Your_Map_Name]["map"] = Map("assets/maps/Your_Map_Name/Your_Map_Name.tmx", game)

    # Load the map foreground .tmx file
    game.maps[Your_Map_Name]]["foreground"] = Map("assets/maps/YYour_Map_Name]/Your_Map_Name]_foreground.tmx", game)

    # Create your map and map foreground surface (img)
    game.maps[Your_Map_Name]["img"] = game.maps[Your_Map_Name]["map"].make()
    game.maps[Your_Map_Name]["fg_img"] = game.maps[Your_Map_Name]["foreground"].make()

    # Create a pygame Rect from the map surface (img)
    game.maps[Your_Map_Name]["rect"] = game.maps[Your_Map_Name]["img"].get_rect()

    # Load the loading screen image for that map
    game.maps[Your_Map_Name]["loading"] = pygame.image.load("assets/img/loading/Your_Map_Name.png")
    ```

5. Create your map warper in the *worldmap.tmx* spawner layer using Tiled

   Your object name in the *spawner* layer needs to have your map name (**respect the casing !**) : 

    *__MapName_warper__*

6. Build a decor around your warper

***
## License
[GNU General Public License v3.0](https://raw.githubusercontent.com/StendWood/Project2_SavalFer/master/LICENSE)
