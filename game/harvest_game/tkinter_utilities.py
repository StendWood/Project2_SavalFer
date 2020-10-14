

from tkinter import *
from seed import Seed

def action_button():
    print("\nLa graine est plantée !\n")

def create_view_seed(window):
    """
        creates the interface with the seed
    """
    # create a frame to put the text
    frame = Frame(window, bg='pink') # bordure → ,bd=1, relief=SUNKEN

    # # create a title
    # choose where and what to print
    label_title = Label(window, text="Graines en stock", font=("Helvetica", 20), bg="grey", fg ="white")
    # print the title on the good place
    label_title.pack(expand=YES)

    # # create another text
    # choose where and what to print, here "Citrouille"
    pumpkin_label = Label(frame, text="Citrouille", font=("Helvetica", 10), bg="pink", fg ="black")
    # print the text on the good place
    pumpkin_label.grid(row=1, column=1, sticky=W)
    # print "Tomate"
    tomato_label = Label(frame, text="Tomate", font=("Helvetica", 10), bg="pink", fg ="black")
    # print the text on the good place
    tomato_label.grid(row=1, column=2,  padx=20, pady=10, sticky=W)


    # # create an image
    # size
    width = 80
    height = 80
    # generate the image
    pumpkin_image = PhotoImage(file="game/harvest_game/img_tkinter/seed_pumpkin.png").zoom(35).subsample(32)
    tomato_image = PhotoImage(file="game/harvest_game/img_tkinter/seed_tomato.png").zoom(35).subsample(32)


    # create a canva to graphic creation, here image of pumpkin seed
    pumpkin_canva = Canvas(frame, width=width, height=height)
    pumpkin_canva.create_image(width/2, height/2, image=pumpkin_image)
    pumpkin_canva.grid(row=2, column=1, sticky=W)
    # create a canva for the image of tomato seed
    tomato_canva = Canvas(frame, width=width, height=height)
    tomato_canva.create_image(width/2, height/2, image=tomato_image)
    tomato_canva.grid(row=2, column=2,  padx=20, pady=10, sticky=W)

    # # add a first button, here for plant pumpkin seed
    pumpkin_button = Button(frame, text="Planter la citrouille", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(4))
    pumpkin_button.grid(row=3, column=1, pady=10, sticky=W)
    # add a button to plant tomato seed
    tomato_button = Button(frame, text="Planter la tomate", font=("helvetica",10), bg = "black", fg ="pink", command=Seed.get_visible(5))
    tomato_button.grid(row=3, column=2, padx=20, pady=10, sticky=W)



    # show the frame
    frame.pack(expand=YES)


    # create a menu bar
    menu_bar = Menu(window)
    # create a menu
    file_menu = Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Ramasser", command=create_view_seed)
    file_menu.add_command(label="Quitter", command=window.quit)
    menu_bar.add_cascade(label= "Fichier", menu=file_menu)
    # show this menu bar on window
    window.config(menu=menu_bar)

    


def tkinter_util():
    # create the first window
    window = Tk()

    # # customiez the first window
    # the name
    window.title("My seeds")
    # the size
    window.geometry("400x200")
    # min and max to avoid the size changement by the player
    window.minsize(400,400)
    window.maxsize(400,400)
    # icon on the right top
    window.iconbitmap("game/harvest_game/img_tkinter/flower_icon.ico")
    # color back ground
    window.config(background='pink')

    return window


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


    # show the first window
    window.mainloop()


if __name__ == "__main__":
    window = tkinter_util()
    create_view_seed(window)