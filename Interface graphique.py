from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

liste = Listbox(fenetre) # Ajout d'une liste avec possibilité de choix
liste.insert(1, "Bonjour")
liste.insert(2, "à")
liste.insert(3, "Tous")
liste.insert(4, "blabla")
liste.insert(5, "test")

liste.pack()


def alert():             # Création du menu supérieur
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre) 

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)


bouton = Checkbutton(fenetre, text="test") # ajout d'un bouton à cocher
bouton.pack()

fenetre.mainloop()

