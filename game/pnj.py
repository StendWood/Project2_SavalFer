# coding: utf-8

# Imports
import pygame
import random

# Additional code
from game.config import *
from game.parents.sprites import Sprites


class Pnj(pygame.sprite.Sprite, Sprites):
    """
        Manage Sprites actions and animations
    """

    # Max 35 strokes
    data = {
        "oldman" : ["Welcome adventurer !", "Stay awhile and listen...",
                    "This farm is known to have the best soil.", "Give it a try !"],
        "farmer" : ["Welcome !", "All this wood for nothing...",
                    "You can cut down a tree if you have the right tool.", "You can cut a log to craft tools."],
        "chicken" : ["Cot Cot Cot !"],
        "rooster" : ["Cocoricoooooooo !"],
        "dog" : ["Woof Woof !", "*The do is asleep...*"],
    }

    def __init__(self, name, can_move, rect, game):
        # Inherit from the Sprite class
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        # Setup attributes
        self.rect = rect
        # hitbox
        self.hitbox_offset_x = 10
        self.hitbox_offset_y = 10
        self.hitbox = pygame.Rect(self.rect.center[0] - self.hitbox_offset_x, self.rect.center[1] - self.hitbox_offset_y, 15, 20)
        # Set the name
        self.name = name
        # Set the current text
        self.text_number = -1
        # Check if vendor of not
        self.is_vendor = False
        if can_move == "true":
            self.can_move = True
            self.velocity = 1
            self.frame = 0
        else:
            self.can_move = False
        if self.can_move:
            # Images
            self.animations_frames = {}
            self.img_path = f"assets/img/pnj/{self.name}/"
            self.image = pygame.image.load(f"assets/img/pnj/{self.name}/idle/idle_0.png")
            # Animation status
            self.status = "idle"
            # self.frame = 0
            self.animation_database = {}
            self.animation_database["idle"] = self.load_animation(
                f"{self.img_path}idle", [120], self.frame, self.animations_frames)
            self.animation_database["run"] = self.load_animation(
                f"{self.img_path}run", [13, 13], self.frame, self.animations_frames)
            self.flip = False
            # Movements
            if random.randint(0, 1) == 1:
                self.is_moving = True
            else:
                self.is_moving = False
            self.movements = ["left", "right", "up", "down"]
            self.direction = random.choice(self.movements)
            self.last_movements_timestamp = pygame.time.get_ticks()

    def update(self):
        """
            Update the pnj position in the world
        """

        if self.can_move:
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

            # Manage movements
            self.random_movements()

    def random_movements(self):
        """
            Manage the random movements of the Pnj, depending on the attributes of movements and time
        """

        # Pnj can move
        if not self.is_moving and pygame.time.get_ticks() - self.last_movements_timestamp >= random.randrange(1000, 3000, 1000):
            # Set pnj movements to moving
            self.is_moving = True
            self.frame, self.status = self.change_action(self.status, "run", self.frame)
            self.direction = random.choice(self.movements)
            if self.direction == "left":
                self.flip = True
            else:
                self.flip = False
            # Timestamp the movement
            self.last_movements_timestamp = pygame.time.get_ticks()
        # Check for 5000ms (5sec)
        elif self.is_moving and pygame.time.get_ticks() - self.last_movements_timestamp >= random.randrange(1000, 5000, 1000):
            self.is_moving = False
            self.frame, self.status = self.change_action(self.status, "idle", self.frame)
            self.last_movements_timestamp = pygame.time.get_ticks()
        elif self.is_moving:
            self.move()

    def move(self):
        """
            Move the rect of the sprite depending on the direction and the velocity
        """

        if self.direction == "left":
            self.hitbox.x -= 3
            if not self.collision_checker(self.game.walls, self.hitbox):
                self.rect.x -= self.velocity
        elif self.direction == "right":
            self.hitbox.x += 3
            if not self.collision_checker(self.game.walls, self.hitbox):
                self.rect.x += self.velocity
        elif self.direction == "up":
            self.hitbox.y -= 3
            if not self.collision_checker(self.game.walls, self.hitbox):
                self.rect.y -= self.velocity
        elif self.direction == "down":
            self.hitbox.y += 3
            if not self.collision_checker(self.game.walls, self.hitbox):
                self.rect.y += self.velocity
        # Update the hitbox
        self.hitbox.x = self.rect.center[0] - self.hitbox_offset_x
        self.hitbox.y = self.rect.center[1] - self.hitbox_offset_y

    def talk_to(self):
        """
            Manage what text is shown when the player interact with the pnj
        """

        # Force showing the first dialog text
        if self.text_number == -1:
            self.text_number = 0
        # Raise the flag to show the popup
        self.game.pnj_popup_flag = True
        # Choose a random dialog text
        self.text_number = random.randint(0, len(self.data[self.name]))
        try:
            # Return that dialog text to show
            return self.data[self.name][self.text_number]
        except IndexError:
            # Show the default starter dialog text if out of range
            self.text_number = 0
            return self.data[self.name][self.text_number]
