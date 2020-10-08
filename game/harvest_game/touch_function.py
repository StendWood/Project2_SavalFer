# coding: utf-8

# additional code:
import variables_harvest as var

class Touch_function():
    """
        manages all the functions when a touch is pressed
    """


    @staticmethod
    def get_visible(id_object):
        """
            put true to the attibut visible (for seed)
        """
        # print(id_object)
        # seed is visible
        for seed in var.seeds:
            if seed.id == id_object:
                seed.visible = True
                #! print(f'seed name :: {seed.name} - visible :: {seed.visible}')

