# ciding: utf-8

# import
from tkinter import *
from game.harvest_game.seed import Seed
import game.harvest_game.variables_harvest as var


class Iu_flower():
    """
        manage interface user for flower
    """

    def __init__(self, link):
        # create the main window with Tkinter
        self.window = Tk()
        # the name
        self.window.title("Flower")
        # the size
        self.window.geometry("400x400")
        # min and max to avoid the size changement by the player
        self.window.minsize(400,400)
        self.window.maxsize(400,400)
        # icon on the right top
        self.window.iconbitmap("game/harvest_game/img_tkinter/flower_icon.ico")
        # color back ground
        self.window.config(background='white')

        # path to image
        self.link = link

        # print the instruction on the top of the window
        label_title = Label(self.window, text="Voici la fleur que tu viens de trouver", font=("Helvetica", 16), bg="purple", fg ="white")
        # print the title on the good place
        label_title.pack()

        
        #initialise view flower
        self.create_view_flower()

        # print title
        self.window.title=""


        # ! self.launch_loop()

    def create_view_flower(self):
        """
            creates the interface with the seed
        """
                
        # create a frame to put the text
        self.frame_flower = Frame(self.window, bg='white')

        # # create an image
        # size
        width = 150
        height = 150
        # generate the image
        flower_image = PhotoImage(file=self.link).zoom(12).subsample(24)

        # create a canva to graphic creation
        flower_canva = Canvas(self.frame_flower, width=width, height=height)
        flower_canva.create_image(width/2, height/2, image=flower_image)
        flower_canva.pack(expand=YES)
        # save the image in the good canva
        flower_canva.img = flower_image

        # # add a button to check
        for flower in var.flowers_objects:
            if flower.image_path == self.link :
                current_flower = flower 

        flower_button = Button(self.frame_flower, text="Vérifier", font=("helvetica",18), bg = "green", fg ="white", command=current_flower.request_api)
        flower_button.pack(expand=YES, pady = 20)

        # # add a button to quit
        quit_button = Button(self.frame_flower, text="Quitter", font=("helvetica",12), bg = "red", fg ="white", command=self.window.quit)
        quit_button.pack(padx = 50, pady = 30)

        # show the frame
        self.frame_flower.pack(expand=YES)


    def launch_loop(self):
        """
            launch the loop
        """
        self.window.mainloop()


# if __name__ == "__main__":
#     for key in var.flowers_dict:
#         name = var.flowers_dict[key]["name"]
#         image_path = var.flowers_dict[key]["image_path"]
#         var.flowers_objects.append(Flower(name, image_path))

#     var.tkinter = Iu_flower(link ="assets/img/api/99-Etlingera-elatior.png")
#     var.tkinter.launch_loop()












    # # create a frame to put the text
    # frame = Frame(window, bg='pink') # bordure → ,bd=1, relief=SUNKEN

    # # # create a title
    # # choose where and what to print
    # label_title = Label(window, text="Graines en stock", font=("Helvetica", 20), bg="grey", fg ="white")
    # # print the title on the good place
    # label_title.pack(expand=YES)

    # # # create another text
    # # choose where and what to print, here "Citrouille"
    # pumpkin_label = Label(frame, text="Citrouille", font=("Helvetica", 10), bg="pink", fg ="black")
    # # print the text on the good place
    # pumpkin_label.grid(row=1, column=1, sticky=W)
    # # print "Tomate"
    # tomato_label = Label(frame, text="Tomate", font=("Helvetica", 10), bg="pink", fg ="black")
    # # print the text on the good place
    # tomato_label.grid(row=1, column=2,  padx=20, pady=10, sticky=W)


    # # # create an image
    # # size
    # width = 80
    # height = 80
    # # generate the image
    # pumpkin_image = PhotoImage(file="game/harvest_game/img_tkinter/seed_pumpkin.png").zoom(35).subsample(32)
    # tomato_image = PhotoImage(file="game/harvest_game/img_tkinter/seed_tomato.png").zoom(35).subsample(32)


    # # create a canva to graphic creation, here image of pumpkin seed
    # pumpkin_canva = Canvas(frame, width=width, height=height)
    # pumpkin_canva.create_image(width/2, height/2, image=pumpkin_image)
    # pumpkin_canva.grid(row=2, column=1, sticky=W)
    # # create a canva for the image of tomato seed
    # tomato_canva = Canvas(frame, width=width, height=height)
    # tomato_canva.create_image(width/2, height/2, image=tomato_image)
    # tomato_canva.grid(row=2, column=2,  padx=20, pady=10, sticky=W)

    # # # add a first button, here for plant pumpkin seed
    # pumpkin_button = Button(frame, text="Planter la citrouille", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(4))
    # pumpkin_button.grid(row=3, column=1, pady=10, sticky=W)
    # # add a button to plant tomato seed
    # tomato_button = Button(frame, text="Planter la tomate", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(5))
    # tomato_button.grid(row=3, column=2, padx=20, pady=10, sticky=W)



    # # show the frame
    # frame.pack(expand=YES)


    # # create a menu bar
    # menu_bar = Menu(window)
    # # create a menu
    # file_menu = Menu(menu_bar,tearoff=0)
    # file_menu.add_command(label="Ramasser", command=create_frame_vegetable)
    # file_menu.add_command(label="Quitter", command=window.quit)
    # menu_bar.add_cascade(label= "Fichier", menu=file_menu)
    # # show this menu bar on window
    # window.config(menu=menu_bar)


    # # show the first window
    # window.mainloop()







    # def create_view_vegetable(self):
    #     """
    #         creates the interface with the seed
    #     """
    #     self.window.title = "Fuits et légumes \nprêts à être ramassés"
    #     self.frame_seed.destroy()
        
    #     # create a frame to put the text
    #     self.frame_vegetable = Frame(self.window, bg='pink') # bordure → ,bd=1, relief=SUNKEN

    #     # # create a title
    #     # choose where and what to print
    #     label_title = Label(self.frame_vegetable, text= self.window.title, font=("Helvetica", 20), bg="grey", fg ="white")
    #     # print the title on the good place
    #     label_title.grid(row=1, column=1, columnspan=2)

    #     # # create another text
    #     # choose where and what to print, here "Citrouille"
    #     flower_label = Label(self.frame_vegetable, text="Citrouille", font=("Helvetica", 10), bg="pink", fg ="black")
    #     # print the text on the good place
    #     flower_label.grid(row=2, column=1)
    #     # print "Tomate"
    #     tomato_label = Label(self.frame_vegetable, text="Tomate", font=("Helvetica", 10), bg="pink", fg ="black")
    #     # print the text on the good place
    #     tomato_label.grid(row=2, column=2,  padx=20, pady=10)


    #     # # create an image
    #     # size
    #     width = 80
    #     height = 80
    #     # generate the image
    #     flower_image = PhotoImage(file="assets/items/vegetable/pumpkin.png").zoom(50).subsample(32)
    #     tomato_image = PhotoImage(file="assets/items/vegetable/tomato.png").zoom(25).subsample(32)


    #     # create a canva to graphic creation, here image of pumpkin seed
    #     pumpkin_canva = Canvas(self.frame_vegetable, width=width, height=height)
    #     pumpkin_canva.create_image(width/2, height/2, image=pumpkin_image)
    #     pumpkin_canva.grid(row=3, column=1)
    #     # save the image in the good canva
    #     pumpkin_canva.img = pumpkin_image
    #     # create a canva for the image of tomato seed
    #     tomato_canva = Canvas(self.frame_vegetable, width=width, height=height)
    #     tomato_canva.create_image(width/2, height/2, image=tomato_image)
    #     tomato_canva.grid(row=3, column=2,  padx=20, pady=10)
    #     # save the image in the good canva
    #     tomato_canva.img = tomato_image

    #     # # add a first button, here for plant pumpkin seed
    #     pumpkin_button = Button(self.frame_vegetable, text="Ramasser la citrouille", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(4))
    #     pumpkin_button.grid(row=4, column=1, pady=10)
    #     # add a button to plant tomato seed
    #     tomato_button = Button(self.frame_vegetable, text="Ramasser la tomate", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(5))
    #     tomato_button.grid(row=4, column=2, padx=20, pady=10)


    #     # show the frame
    #     self.frame_vegetable.pack(expand=YES)


    #     #! # show the main window
    #     # self.mainloop()


    # # @staticmethod
    # # def action_button():
    # #     print("\nLa graine est plantée !\n")

    # def create_view_seed(self):
    #     """
    #         creates the interface with the seed
    #     """
    #     self.window.title = "Graines en stock"
    #     self.frame_vegetable.destroy()

    #     # create a frame to put the text
    #     self.frame_seed = Frame(self.window, bg='pink') # bordure → ,bd=1, relief=SUNKEN

    #     # # create a title
    #     # choose where and what to print
    #     label_title = Label(self.frame_seed, text=self.window.title, font=("Helvetica", 20), bg="grey", fg ="white")
    #     # print the title on the good place
    #     label_title.grid(row=1, column=1, columnspan=2)

    #     # # create another text
    #     # choose where and what to print, here "Citrouille"
    #     pumpkin_label = Label(self.frame_seed, text="Citrouille", font=("Helvetica", 10), bg="pink", fg ="black")
    #     # print the text on the good place
    #     pumpkin_label.grid(row=2, column=1)
    #     # print "Tomate"
    #     tomato_label = Label(self.frame_seed, text="Tomate", font=("Helvetica", 10), bg="pink", fg ="black")
    #     # print the text on the good place
    #     tomato_label.grid(row=2, column=2,  padx=20, pady=10)


    #     # # create an image
    #     # size
    #     width = 80
    #     height = 80
    #     # generate the image
    #     pumpkin_image = PhotoImage(file="game/harvest_game/img_tkinter/seed_pumpkin.png").zoom(32).subsample(32)
    #     tomato_image = PhotoImage(file="game/harvest_game/img_tkinter/seed_tomato.png").zoom(10).subsample(32)


    #     # create a canva to graphic creation, here image of pumpkin seed
    #     pumpkin_canva = Canvas(self.frame_seed, width=width, height=height)
    #     pumpkin_canva.create_image(width/2, height/2, image=pumpkin_image)
    #     pumpkin_canva.grid(row=3, column=1)
    #     # save the image in the good canva
    #     pumpkin_canva.img = pumpkin_image

    #     # create a canva for the image of tomato seed
    #     tomato_canva = Canvas(self.frame_seed, width=width, height=height)
    #     tomato_canva.create_image(width/2, height/2, image=tomato_image)
    #     tomato_canva.grid(row=3, column=2,  padx=20, pady=10)
    #     # save the image in the good canva
    #     tomato_canva.img = tomato_image

    #     # # add a first button, here for plant pumpkin seed
    #     pumpkin_button = Button(self.frame_seed, text="Planter la citrouille", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(4))
    #     pumpkin_button.grid(row=4, column=1, pady=10)
    #     # add a button to plant tomato seed
    #     tomato_button = Button(self.frame_seed, text="Planter la tomate", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(5))
    #     tomato_button.grid(row=4, column=2, padx=20, pady=10)


    #     # show the frame
    #     self.frame_seed.pack(expand=YES)


    #     #! # show the main window
    #     # self.mainloop()


        




