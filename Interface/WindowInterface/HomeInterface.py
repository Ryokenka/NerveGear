from tkinter import *
from Interface.GameEngine.MinecraftTest import MinecraftEngine
from Interface.CapteursEngine.HeadTiltRecognition import HeadTracking
from Interface.CapteursEngine.HeadTiltRecognition import HeadEtHandTracking

import customtkinter as ctk
import csv

MC = MinecraftEngine()

def MCavancer():
    MC.bouger_perso('z', 2, 'avant')
def MCreculer():
    MC.bouger_perso('s', 2, 'arrière')
def MCgauche():
    MC.bouger_perso('q', 2, 'gauche')
def MCdroite():
    MC.bouger_perso('d', 2, 'droit')

def load_config(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        config = []
        for row in reader:
            action = row[0]
            options = row[1:]
            config.append([action, options])
        return config

def load_selected_options():
    with open("../ConfigEngine/selected_options.txt", 'r') as file:
        reader = csv.reader(file)
        config = []
        for row in reader:
            selected = row[0]
            config.append(selected)
        return config

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

        for F in (FrameConfig, FrameBoutons, FrameGuideCapteurs, FrameMonProfil, FrameNervegear):
            self.frames[F] = F(container)
            self.frames[F].grid(row=0, column=0, sticky="nsew")
        self.show_frame(FrameConfig)

    def show_frame(self, cont):
        self.frames[cont].tkraise()

class FrameNavig(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_start = ctk.CTkFrame(self)
        #ici faire fonction de choix des autres fcts
        self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: print(load_selected_options()),
                                    onvalue="on", offvalue="off")
        self.frame_start.pack(pady=20, padx=20)
        self.frame_start.button.pack(pady=20, padx=30)
        self.button1 = ctk.CTkButton(self, text="Configuration", command=lambda: master.show_frame(FrameConfig))
        self.button1.pack(pady=20, padx=20)

        self.button2 = ctk.CTkButton(self, text="Test Commandes", command=lambda: master.show_frame(FrameBoutons))
        self.button2.pack(pady=20, padx=20)

        self.button_guide = ctk.CTkButton(self, text="Guide capteurs",
                                          command=lambda: master.show_frame(FrameGuideCapteurs))
        self.button_guide.pack(pady=20, padx=20)

        self.button_profil = ctk.CTkButton(self, text="Mon profil", command=lambda: master.show_frame(FrameMonProfil))
        self.button_profil.pack(pady=20, padx=20)

        self.button_nervegear = ctk.CTkButton(self, text="Nervegear", command=lambda: master.show_frame(FrameNervegear))
        self.button_nervegear.pack(pady=20, padx=20)

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
        def optionmenu_callback(choice, i):
            print(choice,i)
            with open('../ConfigEngine/selected_options.txt', 'r') as f:
                lines = f.readlines()
            with open('../ConfigEngine/selected_options.txt', 'w') as f:
                for j, line in enumerate(lines):
                    if j == i:
                        f.write(f'{choice}\n')
                    else:
                        f.write(line)

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
                    optionmenu_var = ctk.StringVar(value=lst_selected[i])
                    list.e=ctk.CTkOptionMenu(list, values=lst[i][1],
                                             command=lambda choice, nb=i : optionmenu_callback(choice, nb),
                                             variable=optionmenu_var)

                list.e.grid(row=i, column=j, padx=20, pady=10)

class FrameGuideCapteurs(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.labelMain = (ctk.CTkLabel(self, text="text", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Guide des capteurs", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))

class FrameMonProfil(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Mon profil blabla", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))

class FrameNervegear(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.labelMain = (ctk.CTkLabel(self, text="text", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Nervegear", font=("Courrier", 20))
                          .grid(row=0, padx=20, pady=20))

def StartAllTracking(MC, TableauMapping):
    ListeDesTouches = TableauMapping[0]
    ListeDesCapteurs = TableauMapping[1]
    print("je veux lancer les capteurs : "+ListeDesCapteurs)


def traiter_capteur_eeg():
    print("Traitement pour Capteur EEG - clignement des yeux")

def traiter_capteur_ecg():
    print("Traitement pour Capteur ECG - rythme cardiaque")

def traiter_capteur_emg():
    print("Traitement pour Capteur EMG - bras")

def traiter_webcam_tete_droite():
    print("Traitement pour WebCam tete droite")

def traiter_webcam_tete_gauche():
    print("Traitement pour WebCam tete gauche")

def traiter_webcam_main_un():
    print("Traitement pour main un")

def traiter_webcam_main_deux():
    print("Traitement pour main deux")

def traiter_webcam_main_trois():
    print("Traitement pour main trois")

def traiter_webcam_main_quatre():
    print("Traitement pour main quatre")

def traiter_webcam_main_cinq():
    print("Traitement pour main cinq")


#definition du mapping
if __name__ == "__main__":
    # appeler fichiers ds capteurs selon la configuration

    lst =load_config('../ConfigEngine/config.csv')
    print("yolo")
    lst_selected = load_selected_options()
    total_rows = len(lst)
    app = App()
    app.mainloop()