



# def function_1(arg):
#     print("In function_1")

# def function_2(arg):
#     print("In function_2")

# def function_3(fileName):
#     print("In function_3")
#     return print(fileName)


# def createDictionary():

#     dict = {

#         1 : function_1,
#         2 : function_2,
#         3 : function_3,

#     }    
#     return dict

# dictionary = createDictionary()
# dictionary[3]("test""num""2")#pass any key value to call the method


# import variables_harvest as var

def change_letter(arg = "Par défaut"):
    print(f"changement de H en {arg}")

# for key in var.touch:
#     if key == "espace":
#         print (var.touch.get(key))

# program = 'a = 5\nb=10\nprint("Sum =", a+b)'
# exec(program)


#? fonction dans un dico ET compréhension de dictionnaire #################
# def change_letter(a="A"):
#     print(f"changement de H en {a}")

# test_dico = {
#     "h" : change_letter("I"),
#     "r" : "R"
# }

# (test_dico.value for key in test_dico if key.test_dico == "h")
# print(valeur_cle)
# (test_dico.value for key in test_dico if key.test_dico == "z")
# valeur_cle = (test_dico.value for key in test_dico if key.test_dico == "r")
# print(valeur_cle)
# ? #########################################################################


# import pygame
# running = True
# while running :
#     print("début")
#     pygame.display.set_caption("ok") 
#     window_screen = pygame.display.set_mode((800, 600)) 
#     # window_screen = Pygame_util.generate_window("OK", 800, 600)
#     ## load tiled map 
#     # Map_tiled.render(window_screen,'assets/maps/HarvestLand/HarvestLand.tmx')
#!     imported_image = pygame.image.load('assets/items/vegetable/pumpkin.png')
#!     window_screen.blit(imported_image, (30, 40))
#!     pygame.display.flip()
#     print("fin")
