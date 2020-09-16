# coding: utf-8

# imports
import pygame


class Player(pygame.sprite.Sprite):
    """
        Player class
    """

    def __init__(self, x: int, y: int, img: str):
        """
            Constructor | img: is the path of the avatar files
        """

        # Init the sprite class
        pygame.sprite.Sprite.__init__(self)
        self.health = 100                         # ! = health_player
        self.max_health = 100                         # ! =  max_health_player
        self.velocity = 1                         # ! =  velocity_player
        self.jump_height = 5
        self.jump_velocity = 3
        # Images
        self.animations_frames = {}
        self.img_path = img
        self.image = pygame.image.load(f"{self.img_path}idle_down/idle_down_0.png")
        # Rect
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
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


    def move_right(self):
        """
            Move the player to the right
        """

        # Change player action
        self.change_action("run_side")
        self.flip = False
        # Move the rect
        self.rect.x += self.velocity


    def move_left(self):
        """
            Move the player to the left
        """

        # Change player action
        self.change_action("run_side")
        self.flip = True
        # Move the rect
        self.rect.x -= self.velocity


    def move_up(self):
        """
            Move the player up
        """

        # Change player action
        self.change_action("run_up")
        self.flip = False
        # Move the rect
        self.rect.y -= self.velocity
    

    def move_down(self):
        """
            Move the player down
        """

        # Change player action
        self.change_action("run_down")
        self.flip = False
        # Move the rect
        self.rect.y += self.velocity


    def jump(self):
        """
            the player jumps and go forward
        """

        # Change player action
        # self.change_action("jump")
        # Move the rect
        self.rect.y -= self.jump_height
        self.rect.x += self.jump_velocity


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
