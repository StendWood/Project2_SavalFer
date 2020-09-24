# coding: utf-8

# imports
import pygame

# Additionnal code
from game.data.inventory import Inventory
from game.parents.sprites import Sprites


class Player(pygame.sprite.Sprite, Sprites):
    """
        Player class
    """

    def __init__(self, x: int, y: int, img: str, game):
        """
            Constructor | img: is the path of the avatar files
        """

        # Access game
        self.game = game
        # Init the sprite class
        pygame.sprite.Sprite.__init__(self)

        # Data
        self.id = 1

        # Inventory
        self.inventory = Inventory(game, self.id)
        self.inventory.get_player_object()
        # Stats
        self.velocity = 5

        # Images
        self.animations_frames = {}
        self.img_path = img
        self.image = pygame.image.load(f"{self.img_path}idle_down/idle_down_0.png")

        # Rect
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y

        # hitbox
        self.hitbox_offset_x = 10
        self.hitbox_offset_y = 10
        self.hitbox = pygame.Rect(self.rect.center[0] - self.hitbox_offset_x, self.rect.center[1] - self.hitbox_offset_y, 20, 20)

        # Manage sprite animation
        self.animation_database = {}
        # Animation status
        self.status = "idle_down"
        self.frame = 0
        # Idle
        self.animation_database["idle_down"] = self.load_animation(
            f"{self.img_path}idle_down", [120], self.frame, self.animations_frames)
        self.animation_database["idle_up"] = self.load_animation(
            f"{self.img_path}idle_up", [120], self.frame, self.animations_frames)
        self.animation_database["idle_side"] = self.load_animation(
            f"{self.img_path}idle_side", [120], self.frame, self.animations_frames)
        # Press Z or UP
        self.animation_database["run_up"] = self.load_animation(
            f"{self.img_path}run_up", [13, 13, 13, 13, 13, 13, 13, 13, 13], self.frame, self.animations_frames)
        self.animation_database["run_down"] = self.load_animation(
            f"{self.img_path}run_down", [13, 13, 13, 13, 13, 13, 13, 13, 13], self.frame, self.animations_frames)
        self.animation_database["run_side"] = self.load_animation(
            f"{self.img_path}run_side", [13, 13, 13, 13, 13, 13, 13, 13, 13], self.frame, self.animations_frames)
        # Manage the flip status
        self.flip = False

        # Manage world position
        self.current_map = "worldmap"


    def move(self, new_status: str, direction: str, flip: bool =False):
        """
            Manage the player movements and collisions
        """

        # Change player action
        self.frame, self.status = self.change_action(self.status, new_status, self.frame)
        self.flip = flip
        # Right
        if direction == "right":
            self.hitbox.x += self.velocity
            if not self.collision_checker(self.game.walls, self.hitbox) and \
                self.hitbox.x < self.game.maps[self.current_map]["rect"].width - self.hitbox.w:
                self.rect.x += self.velocity
        #Left
        if direction == "left":
            self.hitbox.x -= self.velocity
            if not self.collision_checker(self.game.walls, self.hitbox) and self.hitbox.x > 0:
                self.rect.x -= self.velocity
        # Down
        if direction == "down":
            self.hitbox.y += self.velocity
            if not self.collision_checker(self.game.walls, self.hitbox) and \
                self.hitbox.y < self.game.maps[self.current_map]["rect"].height - self.hitbox.h:
                self.rect.y += self.velocity
        # Up
        if direction == "up":
            self.hitbox.y -= self.velocity
            if not self.collision_checker(self.game.walls, self.hitbox) and self.hitbox.y > 0:
                self.rect.y -= self.velocity


    def update(self):
        """
            Update the player position
        """

        # Increment the frame
        self.frame += 1
        # Increment the frame for the attack
        # Check if the time of the frame is passed
        if self.frame >= len(self.animation_database[self.status]):
            # Set the frame counter back to 0 for the next image or the attack_frame
            self.frame = 0
        # Find the frame under the current status and get the specific image id for the actual frame
        img_id = self.animation_database[self.status][self.frame]
        self.image = self.animations_frames[img_id]

        # Update the hitbox
        self.hitbox.x = self.rect.center[0] - self.hitbox_offset_x
        self.hitbox.y = self.rect.center[1] - self.hitbox_offset_y

    def save_pos(self):
        """
            Save the player before teleport position to use it when the player teleport back to the worldmap
        """

        self.old_pos = (self.rect.x, self.rect.y)
        print(self.old_pos)
