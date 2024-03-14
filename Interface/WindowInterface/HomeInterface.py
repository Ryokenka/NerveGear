from tkinter import *
from Interface.GameEngine.MinecraftTest import MinecraftEngine

MC = MinecraftEngine()


def MCbouge():
    MC.bouger_perso('z', 2, 'attack')


# Création de la première fenètre
fenetreMain = Tk()
fenetreMain.geometry('720x480')
fenetreMain.title("Interface Test")
fenetreMain['bg'] = 'ivory'
fenetreMain.resizable(height=True, width=True)
fenetreMain.minsize(height="480", width="360")
fenetreMain.iconbitmap("../Image/LOGO_NVG.ico")

labelMain = Label(fenetreMain, text="Interface de configuration", background='ivory', font=("Courrier", 30)).pack(
    side=TOP, padx=50)

# Création du Menu
menuMain = Menu(fenetreMain)
fichier = Menu(menuMain, tearoff=0)
fichier.add_command(label="Jeu")

configuration = Menu(menuMain, tearoff=0)
configuration.add_command(label="Enregistrer la configuration")

menuMain.add_cascade(label="Fichier", menu=fichier)
menuMain.add_cascade(label="Configuration", menu=configuration)
fenetreMain.config(menu=menuMain)

# Création de la frame

frameBd = Frame(fenetreMain, bg="ivory")
btn = Button(frameBd, text='Avancer', font=("Courrier", 25), bg='#96C3CE', fg='black',
             command=MCbouge)
btn.pack(pady=25, fill=X)

frameBd.pack(expand=YES)
fenetreMain.mainloop()
