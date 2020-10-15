# ciding: utf-8

# import
from tkinter import *

def iu_winner():
    # creer la fenetre
    window = Tk()
    window.title("winner")
    window.geometry("720x300")
    window.config(background='blue')

    # creer la frame principale
    frame = Frame(window, bg='#dee5dc')
    # ajout la phrase
    label_winner = Label(frame, text="Tu détiens l'Etlingera elatior ! \nMets-la à l'abris sous l'océan !", font=("Courrier", 30), bg="blue")
    label_winner.pack()

    # ajout du bouton/image
    quit_button = Button(window, text="Quitter", font=("helvetica",12), bg = "red", fg ="white", command=window.quit)
    quit_button.pack(padx = 50, pady = 30)

    # ajout de la frame au centre
    frame.pack(expand=YES)

    # affichage
    window.mainloop()


def iu_loser():
    # creer la fenetre
    window = Tk()
    window.title("loser")
    window.geometry("720x300")
    window.config(background='grey')

    # creer la frame principale
    frame = Frame(window, bg='grey')
    # ajout la phrase
    label_winner = Label(frame, text="Ce n'est pas la bonne fleur...", font=("Courrier", 30), bg="grey")
    label_winner.pack()

    # ajout du bouton/image
    quit_button = Button(window, text="Quitter", font=("helvetica",12), bg = "red", fg ="white", command=window.quit)
    quit_button.pack(padx = 50, pady = 30)

    # ajout de la frame au centre
    frame.pack(expand=YES)

    # affichage
    window.mainloop() 

if __name__ == "__main__":
    # iu_winner()
    iu_loser()