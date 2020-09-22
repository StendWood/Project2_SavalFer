# coding: utf-8

# Imports
import pygame
import pytmx

# Additional codes
from game.data.item import Item


class Inventory:
    """
        Initialise and populate the pplayer inventory
    """

    def __init__(self, game, player_id):
        # give access to game
        self.game = game

        self.player_id = player_id
        # Inventory stats
        self.max_items = 80

        # Player item list
        self.items = []

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
