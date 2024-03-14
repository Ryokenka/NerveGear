from tkinter import *
from Interface.GameEngine.MinecraftTest import MinecraftEngine
import customtkinter as ctk

MC = MinecraftEngine()

def MCavancer():
    MC.bouger_perso('z', 2, 'avant')
def MCreculer():
    MC.bouger_perso('s', 2, 'arrière')
def MCgauche():
    MC.bouger_perso('q', 2, 'gauche')
def MCdroite():
    MC.bouger_perso('d', 2, 'droit')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('720x480')
        self.title("Interface Test")
        self.iconbitmap("../Image/LOGO_NVG.ico")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Interface de configuration", font=("Courrier", 20))
                          .grid(row=0,column=1, padx=20, pady=20))
        # Create CTkFrame
        #menuMain = Menu(self, background="red")
        #fichier = Menu(menuMain, tearoff=0, background="red")
        #fichier.add_command(label="Jeu")

        #configuration = Menu(menuMain, tearoff=0)
        #configuration.add_command(label="Enregistrer la configuration")

        #menuMain.add_cascade(label="Fichier", menu=fichier)
        #menuMain.add_cascade(label="Configuration", menu=configuration)
        #self.config(menu=menuMain)
        self.frame_navig = FrameNavig(self)
        self.frame_navig.grid(column=0, padx=20, pady=20)

        self.frame_boutons = FrameBoutons(self)
        self.frame_boutons.grid(row=1, column=1, padx=20, pady=20)

class FrameNavig(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.button1 = ctk.CTkButton(self, text="Configuration", command=MCavancer)
        self.button1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.button2 = ctk.CTkButton(self, text="Test Commandes", command=MCreculer)
        self.button2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
class FrameBoutons(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.button1 = ctk.CTkButton(self, text="Avancer", command=MCavancer)
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.button2 = ctk.CTkButton(self, text="Reculer", command=MCreculer)
        self.button2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button3 = ctk.CTkButton(self, text="Gauche", command=MCgauche)
        self.button3.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.button4 = ctk.CTkButton(self, text="Droite", command=MCdroite)
        self.button4.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()