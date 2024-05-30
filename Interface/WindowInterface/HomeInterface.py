import threading
from tkinter import *

import pygetwindow as gw


from Interface.CapteursEngine.AccelerometreEngine import AccelerometreTracking
from Interface.CapteursEngine.BitalinoEngine import MuscleTracking
from Interface.CapteursEngine.TestCameraRecognition import HeadAndHandTracking
from Interface.GameEngine.VirtualController import VirtualController

import customtkinter as ctk
import csv
#Test des commandes
MC = VirtualController("Minecraft 1.20.6")
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
    
# Fonction pour sélectionner la fenêtre
def get_active_windows():
    # Retrieve all windows
    windows = gw.getAllTitles()
    # Filter out empty titles and ensure all entries are strings
    return [win for win in windows if isinstance(win, str) and win]

#l'interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1080x720')
        self.title("Interface Test")
        self.iconbitmap("../Image/LOGO_NVG.ico")

        self.selected_window = StringVar(value="Select a window")
        self.window_list = get_active_windows()
        
        # Print the window list to debug
        print("Window List:", self.window_list)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_navig = FrameNavig(self)
        self.frame_navig.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.mainframe = ctk.CTkFrame(self)

        self.labelMain = ctk.CTkLabel(self.mainframe, text="Interface de configuration", font=("Courrier", 25, "bold"))
        self.labelMain.grid(row=0, padx=20, pady=10)

        self.mainframe.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

        self.frames = {}


        for F in (FrameConfig, FrameBoutons, FrameGuideCapteurs, FrameMonProfil, FrameNervegear):
            self.frames[F] = F(self.mainframe)
            self.frames[F].grid(row=0, column=0, sticky="nsew")
        self.show_frame(FrameConfig)

        self.dropdown = ctk.CTkOptionMenu(self.frames[FrameConfig], values=self.window_list, variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, padx=20, pady=20)


    def show_frame(self, cont):
        self.frames[cont].tkraise()
        
    def update_minecraft_window(self, *args):
        selected_window = self.selected_window.get()
        MC.set_window_name(selected_window)
        print(f"Updated Minecraft window to: {selected_window}")

    def get_selected_window(self):
        return self.selected_window.get()

class FrameNavig(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.frame_start = ctk.CTkFrame(self)
        #brouillon : ici faire fonction de choix des autres fcts
        #self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: MuscleTracking(MC.mouvement_clic_muscle, MC.mouvement_saut_muscle),
        #self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: StartAllTracking(),
                                    #onvalue="on", offvalue="off")


        self.switch_var = ctk.BooleanVar(value=False)
        self.buttonTracking = ctk.CTkSwitch(master=self.frame_start, text="Tracking",
                                                    variable=self.switch_var,
                                                    #command = lambda: switch(),
                                                    command=lambda: check_and_start_tracking(self),
                                                    onvalue=True, offvalue=False)


        self.frame_start.pack(pady=20, padx=20)
        self.buttonTracking.pack(pady=20, padx=30)
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

        self.labelMain = (ctk.CTkLabel(self, text="Test Commandes", font=("Courrier", 25))
                          .grid(row=0, padx=20, pady=20, sticky="wn"))

        self.button1 = ctk.CTkButton(self, text="Avancer", command=MCavancer)
        self.button1.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button2 = ctk.CTkButton(self, text="Reculer", command=MCreculer)
        self.button2.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.button3 = ctk.CTkButton(self, text="Gauche", command=MCgauche)
        self.button3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.button4 = ctk.CTkButton(self, text="Droite", command=MCdroite)
        self.button4.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

class FrameConfig(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        list = ctk.CTkScrollableFrame(self)
        list.grid(row=2, column=0, sticky="nsew")

        self.error_label = ctk.CTkLabel(self, text="", font=("Courrier", 12), text_color="Red")
        self.error_label.grid(row=1,column=0, padx=0, pady=0, sticky="nw")


        self.labelMain = (ctk.CTkLabel(self, text="Associer les capteurs aux actions souhaitées", font=("Courrier", 25))
                          .grid(row=0, column=0, padx=20, pady=20, sticky="nw"))



        for i in range(total_rows):
            for j in range(2):
                if j == 0:
                    list.e = ctk.CTkLabel(list, text=lst[i][0])
                else:
                    optionmenu_var = ctk.StringVar(value=lst_selected[i])
                    list.e = ctk.CTkOptionMenu(list, values=lst[i][1],
                                               command=lambda choice, nb=i: write_selected_options(choice, nb),
                                               variable=optionmenu_var)

                list.e.grid(row=i + 1, column=j, padx=20, pady=10, sticky="w")


    def show_error(self, message):
        self.error_label.configure(text=message)
        self.error_label.lift()




class FrameGuideCapteurs(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Guide des capteurs", font=("Courrier", 25))
                          .grid(row=0, padx=20, pady=20, sticky="wn"))
        self.labelText = (ctk.CTkLabel(self, text="Work in progress\n", font=("Courrier", 20))
                          .grid(row=1, padx=20, pady=10, sticky="n"))



class FrameMonProfil(ctk.CTkFrame):
    def create_profile(self):
        pseudo = self.entry_pseudo.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        with open("BDD_pseudo.txt", "a") as file:
            file.write(f"Pseudo: {pseudo}, Email: {email}, Password: {password}\n")

        print("Profil enregistré dans BDD_pseudo.txt.")

    def login(self):
        pseudo = self.entry_pseudo.get()
        password = self.entry_password.get()

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.labelMain = (ctk.CTkLabel(self, text="Mon profil", font=("Courrier", 25))
                          .grid(row=1, column=0, padx=20, pady=20, sticky="nw"))

        self.label_pseudo = (ctk.CTkLabel(self, text="Pseudo:", font=("Courrier", 15))
                             .grid(row=2, column=0, padx=20, pady=10, sticky="nw"))
        self.entry_pseudo = ctk.CTkEntry(self)
        self.entry_pseudo.grid(row=2, column=1, padx=20, pady=10, sticky="nw")

        self.label_email = (ctk.CTkLabel(self, text="Email:", font=("Courrier", 15))
                            .grid(row=3, column=0, padx=20, pady=10, sticky="nw"))
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.grid(row=3, column=1, padx=20, pady=10, sticky="nw")

        self.label_password = (ctk.CTkLabel(self, text="Password:", font=("Courrier", 15))
                               .grid(row=4, column=0, padx=20, pady=10, sticky="nw"))
        self.entry_password = ctk.CTkEntry(self, show="*")
        self.entry_password.grid(row=4, column=1, padx=20, pady=10, sticky="nw")

        self.button_create_profile = ctk.CTkButton(self, text="Créer le profil", command=self.create_profile)
        self.button_create_profile.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        self.button_login = ctk.CTkButton(self, text="Se connecter", command=self.login)
        self.button_login.grid(row=5, column=0, padx=20, pady=10, sticky="w")




class FrameNervegear(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.labelMain = (ctk.CTkLabel(self, text="Nervegear\n", font=("Courrier", 25))
                          .grid(row=0, padx=20, pady=10, sticky="nw"))
        self.labelText = (ctk.CTkLabel(self,
                                       text="Une nouvelle forme de contrôle \n",
                                       font=("Courrier", 20))
                          .grid(row=1, padx=20, pady=10, sticky="s"))
        self.labelText = (ctk.CTkLabel(self, text="Création d’un produit innovant\nAssociation de plusieurs "
                                                  "technologies\nCréation d’un logiciel interface Human-Computer",
                                       font=("Courrier", 15))
                          .grid(row=2, padx=20, pady=10))

        self.labelText = (ctk.CTkLabel(self,
                                       text="\nAdaptabilité\n",
                                       font=("Courrier", 20))
                          .grid(row=3, padx=20, pady=10, sticky="s"))

        self.labelText = (ctk.CTkLabel(self,
                                       text="Aux jeux célèbres : \nPossibilité de jouer à plusieurs jeux : Mario, "
                                            "Minecraft…\n\nA la personne :\nPossibilité d’adapter le logiciel en "
                                            "fonction de la personne et des positionnements des capteurs",
                                       font=("Courrier", 15))
                          .grid(row=4, padx=20, pady=10))

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

def check_and_start_tracking(self):
    if isChoicesValid():
         StartAllTracking()
         app.frames[FrameConfig].show_error("")
    else:
        app.frames[FrameConfig].show_error("Certains choix sont invalides")
        #app.frames[FrameNavig].switch_var = ctk.BooleanVar(value=False)

        bouton_trouve = self.buttonTracking

        if bouton_trouve is not None:
            bouton_trouve.deselect()
            print(bouton_trouve)
        else:
            print("pas trouvé")



def isChoicesValid():
    print("isChoicesValid")
    val = load_selected_options()
    if all(choice == "Veuillez choisir" for choice in val):
        print("Tous les choix sont 'Veuillez choisir'.")
        return False

    #todo : ajouter les autres vérifications : ex : ?

    else :
        print("Tous les choix sont valides")
        return True
def StartAllTracking():
    print("StartAllTracking\n")
    val = load_selected_options()


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
        "Accelerometre": [],
        "Camera": [],
        "EEG": [],
        "EMG": [],
        "ECG": []
    }

    sensor_methode = {
        "Accelerometre": [],
        "Camera": [],
        "EEG": [],
        "EMG": [],
        "ECG": []
    }

    # Remplissage du dictionnaire des utilisations des capteurs en utilisant les indices de val
    for i, value in enumerate(val):
        if "Accelerometre" in value:
            sensor_usage["Accelerometre"].append(sensor_uses[i])
            sensor_methode["Accelerometre"].append(val[i])
        elif "Camera" in value:
            sensor_usage["Camera"].append(sensor_uses[i])
            sensor_methode["Camera"].append(val[i])
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

    tabthread = []

    for sensor, uses in sensor_usage.items():
        if uses:
            if sensor == "Camera":
                tabthread.append(threading.Thread(target=start_camera(*uses, methodes=sensor_methode["Camera"])))
            elif sensor == "Accelerometre":
                tabthread.append(
                    threading.Thread(target=start_accelerometre(*uses, methodes=sensor_methode["Accelerometre"])))
            elif sensor == "EEG":
                tabthread.append(threading.Thread(target=start_eeg(*uses, methodes=sensor_methode["EEG"])))
            elif sensor == "EMG":
                tabthread.append(threading.Thread(target=start_emg(*uses, methodes=sensor_methode["EMG"])))
            elif sensor == "ECG":
                tabthread.append(threading.Thread(target=start_eeg(*uses, methodes=sensor_methode["ECG"])))

    for thread in tabthread:
        thread.start()

    for thread in tabthread:
        thread.join()



def start_camera(*usages, methodes=None):
    #Déplacement / changer d'objet avec main ou eye tracking

    if len(usages) == 1 and methodes[0].strip()=="Camera":
        HeadAndHandTracking(
            lambda: MC.mouvement_gauche_droite_cam("gauche"),
            lambda: MC.mouvement_gauche_droite_cam("milieu"),
            lambda: MC.mouvement_gauche_droite_cam("droite"),
            None
        )

    elif len(usages) ==1 and methodes[0].strip()=="Camera - doigts":
        HeadAndHandTracking(
            None,
            None,
            None,
            lambda number: MC.changer_barre(number)
        )

    elif len(usages) ==1 and methodes[0].strip=="Camera - Eye tracking":
        #todo eye tracking
        print("TO DO EYE TRACKING")

    elif len(usages) == 2:
        if methodes[1].strip() == "Camera - doigts":
            HeadAndHandTracking(
                lambda: MC.mouvement_gauche_droite_cam("gauche"),
                lambda: MC.mouvement_gauche_droite_cam("milieu"),
                lambda: MC.mouvement_gauche_droite_cam("droite"),
                lambda number: MC.changer_barre(number)
            )
        else:
            # todo eye tracking
            print("TO DO EYE TRACKING")


def start_accelerometre(*usages, methodes=None):
    if len(usages) == 1 and methodes[0].strip()=="Accelerometre":
        AccelerometreTracking(
            lambda: MC.clic_deplacements("avant"),
            lambda: MC.clic_deplacements("arriere"),
            lambda: MC.clic_deplacements("gauche"),
            lambda: MC.clic_deplacements("droite"),
            lambda: MC.clic_deplacements("rien")
        )

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
    #sauter avec 1 ou 2 implusions , cliquer avec 1 ou 2 implusions

    if len(usages)==1 and usages[0] =="Sauter" :
        if methodes == "EMG - bras 1 impulsion" :
            MuscleTracking(MC.mouvement_saut_muscle)
        if methodes == "EMG - bras 2 impulsions"  :
            MuscleTracking(None, MC.mouvement_saut_muscle)

    elif len(usages)==1 and usages[0] =="Clique souris" :
        if methodes == "EMG - bras 1 impulsion" :
            MuscleTracking(MC.mouvement_clic_muscle)
        if methodes == "EMG - bras 2 impulsions"  :
            MuscleTracking(None, MC.mouvement_clic_muscle)


    elif len(usages)==2 :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(MC.mouvement_saut_muscle, MC.mouvement_clic_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(MC.mouvement_clic_muscle, MC.mouvement_saut_muscle)



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