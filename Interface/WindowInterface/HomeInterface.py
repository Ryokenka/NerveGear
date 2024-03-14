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
        self.geometry('1080x720')
        self.title("Interface Test")
        self.iconbitmap("../Image/LOGO_NVG.ico")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_navig = FrameNavig(self)
        self.frame_navig.grid(row=0,column=0, padx=20, pady=20, sticky="ns")
        self.frame_navig.grid_rowconfigure(0, weight=1)
        self.frame_navig.configure(width=140, corner_radius=0)

        self.mainframe = ctk.CTkFrame(self)

        self.labelMain = (ctk.CTkLabel(self.mainframe, text="Interface de configuration", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))
        container = ctk.CTkFrame(self.mainframe)
        container.grid(row=1, padx=20, pady=20)

        self.mainframe.grid(row=0,column=1, padx=20, pady=20, sticky="nsew")

        self.frames = {}

        for F in (FrameBoutons, FrameConfig):
            self.frames[F] = F(container)
            self.frames[F].grid(row=0, column=0, sticky="nsew")
        self.show_frame(FrameBoutons)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class FrameNavig(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.button1 = ctk.CTkButton(self, text="Configuration", command=lambda: master.show_frame(FrameConfig))
        self.button1.pack(pady=20, padx=20)

        self.button2 = ctk.CTkButton(self, text="Test Commandes", command=lambda: master.show_frame(FrameBoutons))
        self.button2.pack(pady=20, padx=20)

class FrameBoutons(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.button1 = ctk.CTkButton(self, text="Avancer", command=MCavancer)
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.button2 = ctk.CTkButton(self, text="Reculer", command=MCreculer)
        self.button2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button3 = ctk.CTkButton(self, text="Gauche", command=MCgauche)
        self.button3.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.button4 = ctk.CTkButton(self, text="Droite", command=MCdroite)
        self.button4.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

class FrameConfig(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.button1 = ctk.CTkButton(self, text="Configurer")
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()