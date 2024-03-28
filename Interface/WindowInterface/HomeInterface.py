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

#l'interface
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

        self.mainframe = ctk.CTkFrame(self)

        self.labelMain = (ctk.CTkLabel(self.mainframe, text="Interface de configuration", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))
        container = ctk.CTkFrame(self.mainframe)
        container.grid(row=1, padx=20, pady=20, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.mainframe.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(1, weight=1)

        self.frames = {}

        for F in (FrameConfig, FrameBoutons):
            self.frames[F] = F(container)
            self.frames[F].grid(row=0, column=0, sticky="nsew")
        self.show_frame(FrameConfig)

    def show_frame(self, cont):
        self.frames[cont].tkraise()

class FrameNavig(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.button1 = ctk.CTkButton(self, text="Configuration", command=lambda: master.show_frame(FrameConfig))
        self.button1.pack(pady=20, padx=20)

        self.button2 = ctk.CTkButton(self, text="Test Commandes", command=lambda: master.show_frame(FrameBoutons))
        self.button2.pack(pady=20, padx=20)

class FrameBoutons(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

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
        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        ctk.CTkFrame.__init__(self, master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        list=ctk.CTkScrollableFrame(self)
        list.grid(row=0, column=0, sticky="nsew")

        for i in range(total_rows):
            for j in range(2):
                if j ==0:
                    list.e=ctk.CTkLabel(list, text=lst[i][0])
                else:
                    optionmenu_var = ctk.StringVar(value=lst[i][1][0])
                    list.e=ctk.CTkOptionMenu(list, values=lst[i][1],
                                             command=optionmenu_callback,
                                             variable=optionmenu_var)

                list.e.grid(row=i, column=j, padx=20, pady=10)


#definition du mapping
if __name__ == "__main__":
    lst = [["Touche Avancer", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche Gauche", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche Droite", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche Reculer", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche Sauter", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche Action 1", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche Action 2", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche F1", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche F2", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche F3", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche F4", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche F5", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],
           ["Touche F6", ["Capteur EEG","Capteur ECG","Capteur EMG","WebCam"]],]

    # appeler fichiers ds capteurs selon la configuration


    total_rows = len(lst)
    app = App()
    app.mainloop()