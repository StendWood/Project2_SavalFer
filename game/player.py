# coding: utf-8

# imports
import pygame
from pygame.sprite import collide_rect


class Player(pygame.sprite.Sprite):
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
        # Stats
        self.health = 100                         # ! = health_player
        self.max_health = 100                         # ! =  max_health_player
        self.velocity = 5                        # ! =  velocity_player
        self.jump_height = 5
        self.jump_velocity = 10

        # Images
        self.animations_frames = {}
        self.img_path = img
        self.image = pygame.image.load(f"{self.img_path}idle_down/idle_down_0.png")

        # Rect
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y

        # hitbox
        self.hitbox_offset_x = 7
        self.hitbox_offset_y = 15
        self.hitbox = pygame.Rect(self.rect.center[0] - self.hitbox_offset_x, self.rect.center[1] - self.hitbox_offset_y, 15, 40)

        # Manage sprite animation
        self.animation_database = {}
        # Idle
        self.animation_database["idle_down"] = self.load_animation(f"{self.img_path}idle_down", [120])
        self.animation_database["idle_up"] = self.load_animation(f"{self.img_path}idle_up", [120])
        self.animation_database["idle_side"] = self.load_animation(f"{self.img_path}idle_side", [120])
        # Press Z or UP
        self.animation_database["run_up"] = self.load_animation(f"{self.img_path}run_up", [13, 13, 13, 13, 13, 13, 13, 13, 13])
        self.animation_database["run_down"] = self.load_animation(f"{self.img_path}run_down", [13, 13, 13, 13, 13, 13, 13, 13, 13])
        self.animation_database["run_side"] = self.load_animation(f"{self.img_path}run_side", [13, 13, 13, 13, 13, 13, 13, 13, 13])
        # Animation status
        self.status = "idle_down"
        self.frame = 0
        # Manage the flip status
        self.flip = False

        # Manage world position
        self.current_map = "worldmap"


    def move(self, action: str, direction: str, flip: bool =False):
        """
            Manage the player movmeents and collisions
        """

        # Change player action
        self.change_action(action)
        self.flip = flip
        # Right
        if direction == "right":
            self.hitbox.x += self.velocity
            if not self.collision_checker() and self.hitbox.x < self.game.maps["worldmap"]["rect"].width - self.hitbox.w:
                self.rect.x += self.velocity
        #Left
        if direction == "left":
            self.hitbox.x -= self.velocity
            if not self.collision_checker() and self.hitbox.x > 0:
                self.rect.x -= self.velocity
        # Down
        if direction == "down":
            self.hitbox.y += self.velocity
            if not self.collision_checker() and self.hitbox.y < self.game.maps["worldmap"]["rect"].height - self.hitbox.h:
                self.rect.y += self.velocity
        # Up
        if direction == "up":
            self.hitbox.y -= self.velocity
            if not self.collision_checker() and self.hitbox.y > 0:
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


    def collision_checker(self):
        """
            Check collision between any obstacles and any sprites
        """

        for wall in self.game.walls:
            if self.hitbox.colliderect(wall.rect):
                return True
