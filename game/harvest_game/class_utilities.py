# coding: utf-8

# ! ################# ! #
# !     not used      ! #
# !  must be deleted  ! #
# ! ################# ! #


# additional code
from game.harvest_game.database_utilities import Database
from game.harvest_game.seed import Seed
import game.harvest_game.variables_harvest as var

class Class_util():
    """
        manages the creation of class from database
        (Generic class for classe models)
    """
    

    @staticmethod
    def instantiate_class(collection_name, database_name, fields_db, class_name, needed_result = True):

        # gets datas from the database
        collection_name = f'{database_name}'.execute_query(f"SELECT {fields_db} FROM seed", needed_result)
        # save the datas in items collection
        list_name = [class_name(item) for item in collection_name]
        return list_name
        


if __name__ == "__main__":
    db = Database()
    seeds = Class_util.instantiate_class("seeds_db", f'{db}', "*", f'{Seed}', needed_result = True)
    print(f'les graines :: {seeds}')

