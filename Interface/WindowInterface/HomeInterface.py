from tkinter import *

from Interface.CapteursEngine.BitalinoEngine import MuscleTracking
from Interface.GameEngine.MinecraftTest import MinecraftEngine
from Interface.CapteursEngine.HeadTiltRecognition import HeadTracking
from Interface.CapteursEngine.HeadTiltRecognition import HeadEtHandTracking

import customtkinter as ctk
import csv
#Test des commandes
MC = MinecraftEngine()
def MCavancer():
    MC.bouger_perso('z', 2, 'avant')
def MCreculer():
    MC.bouger_perso('s', 2, 'arrière')
def MCgauche():
    MC.bouger_perso('q', 2, 'gauche')
def MCdroite():
    MC.bouger_perso('d', 2, 'droit')
def MCjump():
    MC.clic_rapide('space')

def load_config(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        config = []
        for row in reader:
            action = row[0]
            options = row[1:]
            config.append([action, options])
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
        #self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: MuscleTracking(MC.mouvement_clic_muscle, MC.mouvement_saut_muscle),
        #self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: StartAllTracking(),
                                    #onvalue="on", offvalue="off")
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
        ctk.CTkFrame.__init__(self, master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")

        for i in range(total_rows):
            for j in range(2):
                if j == 0:
                    label = ctk.CTkLabel(self.scrollable_frame, text=lst[i][0])
                    label.grid(row=i, column=j, padx=20, pady=10)
                else:
                    optionmenu_var = ctk.StringVar(value=lst_selected[i])
                    option_menu = ctk.CTkOptionMenu(self.scrollable_frame, values=lst[i][1],
                                                     command=lambda choice, nb=i: write_selected_options(choice, nb),
                                                     variable=optionmenu_var)
                    option_menu.grid(row=i, column=j, padx=20, pady=10)





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

def load_selected_options():
    with open("../ConfigEngine/selected_options.txt", 'r') as file:
        reader = csv.reader(file)
        config = []
        for row in reader:
            selected = row[0]
            config.append(selected)
        return config


def write_selected_options(choice, i):
    print("write")
    with open('../ConfigEngine/selected_options.txt', 'r') as f:
        lines = f.readlines()
    with open('../ConfigEngine/selected_options.txt', 'w') as f:
        for j, line in enumerate(lines):
            if j == i:
                f.write(f'{choice}\n')
            else:
                f.write(line)
def StartAllTracking():
    print("StartAllTracking\n")

    val = load_selected_options()

    for i, value in enumerate(val):
        print(f"Valeur {i + 1} :", value)

    # Liste des utilisations des capteurs
    sensor_uses = [
        "Déplacement",
        "Vitesse",
        "Sauter",
        "Clique souris",
        "Changer d'objet"
    ]

    # Initialisation du dictionnaire des utilisations des capteurs
    sensor_usage = {
        "Camera": [],
        "Accelerometre": [],
        "EEG": [],
        "EMG": [],
        "ECG": []
    }

    sensor_methode = {
        "Camera": [],
        "Accelerometre": [],
        "EEG": [],
        "EMG": [],
        "ECG": []
    }

    # Remplissage du dictionnaire des utilisations des capteurs en utilisant les indices de val
    for i, value in enumerate(val):
        if "Camera" in value:
            sensor_usage["Camera"].append(sensor_uses[i])
            sensor_methode["Camera"].append(val[i])
        elif "Accelerometre" in value:
            sensor_usage["Accelerometre"].append(sensor_uses[i])
            sensor_methode["Accelerometre"].append(val[i])
        elif "EEG" in value:
            sensor_usage["EEG"].append(sensor_uses[i])
            sensor_methode["EEG"].append(val[i])
        elif "EMG" in value:
            sensor_usage["EMG"].append(sensor_uses[i])
            sensor_methode["EMG"].append(val[i])
        elif "ECG" in value:
            sensor_usage["ECG"].append(sensor_uses[i])
            sensor_methode["ECG"].append(val[i])
        elif "Veuillez choisir" in value:
            print("Aucun choix")
        else:
            print("Choix non reconnu :", value)



    for sensor, uses in sensor_usage.items():
        if uses:
            if sensor == "Camera":
                start_camera(*uses, methodes=sensor_methode["Camera"])
            elif sensor == "Accelerometre":
                start_accelerometre(*uses, methodes=sensor_methode["Accelerometre"])
            elif sensor == "EEG":
                start_eeg(*uses, methodes=sensor_methode["EEG"])
            elif sensor == "EMG":
                start_emg(*uses, methodes=sensor_methode["EMG"])
            elif sensor == "ECG":
                start_ecg(*uses, methodes=sensor_methode["ECG"])


def start_camera(*usages, methodes=None):
    #Déplacement / changer d'objet avec main ou eye tracking
    print("Démarrage de la caméra.")
    for usage in usages:
        print(f"Utilisation de la caméra pour : {usage}")

    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")

def start_accelerometre(*usages, methodes=None):
    #Deplacement
    print("Démarrage de l'accéléromètre.")
    for usage in usages:
        print(f"Utilisation de l'accéléromètre pour : {usage}")

    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")


def start_eeg(*usages, methodes=None):
    #Sauter
    print("Démarrage de l'EEG.")
    for usage in usages:
        print(f"Utilisation de l'EEG pour : {usage}")
    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")

def start_emg(*usages, methodes=None):
    #sauter avec 1 ou 2 implusions
    print("Démarrage de l'EMG.")
    for usage in usages:
        print(f"Utilisation de l'EMG pour : {usage}")
    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")


def start_ecg(*usages, methodes=None):
    #vitesse
    print("Démarrage de l'ECG.")
    for usage in usages:
        print(f"Utilisation de l'ECG pour : {usage}")
    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")



#definition du mapping
if __name__ == "__main__":
    # appeler fichiers ds capteurs selon la configuration

    lst =load_config('../ConfigEngine/config.csv')
    lst_selected = load_selected_options()
    total_rows = len(lst)
    app = App()
    app.mainloop()