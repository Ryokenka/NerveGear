from tkinter import *





#Création de la première fenètre 
fenetreMain =Tk()
fenetreMain.geometry('500x500')
fenetreMain.title("Interface Test")
fenetreMain['bg']='ivory'
fenetreMain.resizable(height=True,width=True)
fenetreMain.minsize(height="480",width="360")

labelMain = Label(fenetreMain, text="Interface de configuration",background='ivory', font=("Courrier",30)).pack(side=TOP,padx=50)

#Création du Menu
menuMain = Menu(fenetreMain)
fichier = Menu(menuMain,tearoff=0)
fichier.add_command(label="Jeu")

configuration = Menu(menuMain,tearoff=0)
configuration.add_command(label="Enregistrer la configuration")

menuMain.add_cascade(label="Fichier",menu=fichier)
menuMain.add_cascade(label="Configuration",menu=configuration)



fenetreMain.config(menu=menuMain)
fenetreMain.mainloop()