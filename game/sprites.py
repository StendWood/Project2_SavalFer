# coding: utf-8

# Imports
import pygame
import random

# Additional code
from game.config import *


class Sprites(pygame.sprite.Sprite):
    """
        Manage every pnj method
    """

    data = {
        
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
        self.name = name
        if can_move == "true":
            self.can_move = True
            self.velocity = 1
        else:
            self.can_move = False
        if self.can_move:
            # Images
            self.animations_frames = {}
            self.img_path = f"img/pnj/{self.name}/"
            self.image = pygame.image.load(f"img/pnj/{self.name}/idle/idle_0.png")
            # Animation status
            self.status = "idle"
            self.frame = 0
            self.animation_database = {}
            self.animation_database["idle"] = self.load_animation(f"{self.img_path}idle", [120])
            self.animation_database["run"] = self.load_animation(f"{self.img_path}run", [13, 13])
            self.flip = False
            # Movements
            self.is_moving = False
            self.movements = ["left", "right", "up", "down"]
            self.direction = random.choice(self.movements)
            self.last_movements_timestamp = pygame.time.get_ticks()

    def load_animation(self, path: str, frame_durations: list):
        """
            Calculate the images needed to animate the player.
            path is the folder where the images are.
            frame_durations is a list of how many frames each images show. 
                Ex: [7, 7, 40] => meaning 7s , 7s and 40s
        """

        # Save the animation name
        animation_name = path.split("/")[-1]
        # Save each frame time
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            # Check each frames
            animation_frame_id = animation_name + "_" + str(n)
            # Get the image location
            img_loc = path + "/" + animation_frame_id + ".png"
            # Get the image and convert
            animation_image = pygame.image.load(img_loc).convert_alpha()
            self.animations_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1

        return animation_frame_data

    def change_action(self, new_value):
            """
                Manage frames and status changes on player actions
            """
            if self.status != new_value:
                self.status = new_value
                self.frame = 0

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
            Manage the random movements of the Pnj, depending on the attributes of movements
        """

        # Pnj can move
        if not self.is_moving and pygame.time.get_ticks() - self.last_movements_timestamp >= 3000:
            # Set pnj movements to moving
            self.is_moving = True
            self.change_action("run")
            self.direction = random.choice(self.movements)
            if self.direction == "left":
                self.flip = True
            else:
                self.flip = False
            # Timestamp the movement
            self.last_movements_timestamp = pygame.time.get_ticks()
        # Check for 5000ms (5sec)
        elif self.is_moving and pygame.time.get_ticks() - self.last_movements_timestamp >= 1000:
            self.is_moving = False
            self.change_action("idle")
            self.last_movements_timestamp = pygame.time.get_ticks()
        elif self.is_moving:
            self.move()

    def move(self):
        """
            Move the rect of the sprite depending on the direction and the velocity
        """

        if self.direction == "left":
            self.hitbox.x -= 3
            if not self.collision_checker():
                self.rect.x -= self.velocity
        elif self.direction == "right":
            self.hitbox.x += 3
            if not self.collision_checker():
                self.rect.x += self.velocity
        elif self.direction == "up":
            self.hitbox.y -= 3
            if not self.collision_checker():
                self.rect.y -= self.velocity
        elif self.direction == "down":
            self.hitbox.y += 3
            if not self.collision_checker():
                self.rect.y += self.velocity
        # Update the hitbox
        self.hitbox.x = self.rect.center[0] - self.hitbox_offset_x
        self.hitbox.y = self.rect.center[1] - self.hitbox_offset_y

    def collision_checker(self):
        """
            Check collision between any obstacles and any sprites
        """

        for wall in self.game.walls:
            if self.hitbox.colliderect(wall.rect):
                return True

    def talk_to(self):
        """
            Manage what text is shown when the player interact with the pnj
        """

        pass

    def debug_show_rect(self):
        """
            Show the rects in red for debug purpose
        """

        pygame.draw.rect(self.game.screen, (255, 0, 0), self.game.camera.apply_rect(self.rect), 2)
