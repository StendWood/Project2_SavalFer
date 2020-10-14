# coding: utf-8

# Imports
import pygame
from pygame.constants import SRCALPHA
import pytmx

# Additional codes
from game.data.item import Item
import game.harvest_game.variables_harvest as var


class Inventory:
    """
        Initialise and populate the pplayer inventory
    """

    def __init__(self, game, player_id):
        # give access to game
        self.game = game
        self.inventory_bg = pygame.image.load("assets/img/inventory/bg.png").convert_alpha()
        self.player_id = player_id
        # Inventory stats
        self.max_items = 80

        # Player item list
        self.items = []

        # Tooltip
        self.tooltip_img = pygame.image.load("assets/img/inventory/tooltip.png")
        self.tooltip_x = 200
        self.tooltip_y = 75
        self.tooltip_surface = pygame.Surface((self.tooltip_x, self.tooltip_y), SRCALPHA)
        self.tooltip_surface.blit(self.tooltip_img, (0, 0))

    def get_player_object(self):
        """
            Ask the database for the player items and instanciate every items
        """

        # Ask the DB
        items_list = self.game.db.global_query(
            f"""
                SELECT o.name, o.attack, o.type, o.image_path FROM "Projet_2".user u
                INNER JOIN "Projet_2".user_object uo ON u.user_id = uo.fk_user_id
                INNER JOIN "Projet_2".object o ON o.object_id = uo.fk_object_id
                WHERE u.user_id = {self.player_id};
            """,
        )
        # Create the player items
        for item in items_list:
            self.items.append(
                Item(item[0], item[1], item[2], item[3])
                )
        
        self.place_items_in_inventory()

    def place_items_in_inventory(self):
        """
            Generate the items positions in the player inventory
        """

        inventory_rect = pygame.Rect((50, 50), (self.inventory_bg.get_width(), self.inventory_bg.get_height()))
        i = 0
        offset_x = 75
        offset_y = 100
        # Blit the items into the inventory page
        for item in self.items:
            item.rect.x = inventory_rect.x + offset_x
            item.rect.y = inventory_rect.y + offset_y
            i += 1
            offset_x+= 55
            if i == 10:
                offset_x = 75
                offset_y += 50
                i = 0

    def item_mouseover(self):
        """
            Show inventory item tooltip on mouseover
        """

        # Check every item for collision
        for item in self.items:
            if item.image.get_rect(x=item.rect.x, y=item.rect.y).collidepoint(pygame.mouse.get_pos()):
                # 
                for info in item.tooltip:
                    self.tooltip_surface.blit(
                        self.game.inventory_font.render(
                        info.capitalize(), True, (0, 0, 0)),
                        (10, 20*item.tooltip.index(info) + 5)
                    )
                self.game.screen.blit(
                    self.tooltip_surface,
                    (pygame.mouse.get_pos()[0],
                    pygame.mouse.get_pos()[1] - self.tooltip_y,))
            else:
                # Clear the tooltip surface from any previous text
                self.tooltip_surface.blit(self.tooltip_img, (0, 0))

    def add_item(self, id_item):
        """
            adds item in inventory
        """

        for seed in var.seeds:
            if id_item == seed.id:
                name = seed.name
                image_path = seed.link

        self.items.append(Item(name=name, attack =0, image_path=image_path))
