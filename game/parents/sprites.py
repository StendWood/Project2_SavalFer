# coding: utf-8

# Imports
import pygame
import random

# Additional code
from game.config import *


class Sprites:
    """
        Manage Sprites actions and animations
    """

    # Class attributes

    @classmethod
    def load_animation(cls, path: str, frame_durations: list, frame : int, animations_frames : dict):
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
            animations_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1

        return animation_frame_data

    @classmethod
    def change_action(cls, status, new_status, frame):
            """
                Manage frames and status changes on player actions
            """

            if status != new_status:
                return 0, new_status
            else:
                return frame, status

    @classmethod
    def collision_checker(cls, walls, hitbox):
        """
            Check collision between any obstacles and any sprites
        """

        for wall in walls:
            if hitbox.colliderect(wall.rect):
                return True

    @classmethod
    def show_text_popup(cls, player, game):
        """
            Check if the warper rect is touching the player rect => Show a prompt to let the player enter a new map
        """

        # Check for collision
        if player.rect.colliderect(player.rect):
            # Set warper collision to True
            game.pnj_popup_flag = True

    @classmethod
    def debug_show_rect(cls, screen, camera, rect):
        """
            Show the rects in red for debug purpose
        """

        pygame.draw.rect(screen, (255, 0, 0), camera.apply_rect(rect), 2)
