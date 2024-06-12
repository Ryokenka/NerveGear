import inspect
from tkinter import *
from typing import Dict, List, Any

import pygetwindow as gw
from multiprocessing import Pool, cpu_count
from Interface.CapteursEngine.AccelerometreEngine import AccelerometreTracking
from Interface.CapteursEngine.BitalinoEngine import MuscleTracking
from Interface.CapteursEngine.TestCameraRecognition import HeadAndHandTracking
from Interface.GameEngine.VirtualController import VirtualController
from Interface.WindowInterface.Frames import FrameGuideCapteurs
from Interface.WindowInterface.Frames import FrameConfig
from Interface.WindowInterface.Frames import FrameBoutons
from Interface.WindowInterface.Frames import FrameNervegear
from Interface.WindowInterface.Frames import FrameMonProfil
from Interface.WindowInterface.Frames import FrameConfigAdvance
from Interface.ConfigEngine import ConfigEncryption
import pyperclip
from tkinter import Text

import customtkinter as ctk
import csv

from Interface.WindowInterface.utils import load_selected_options

MC = VirtualController("")
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



        self.selected_window = StringVar(value="Choisir fenêtre")
        self.window_list = get_active_windows()
        self.update_minecraft_window(self)

        # Print the window list to debug
        print("Window List:", self.window_list)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.total_rows = total_rows # Example shared variable
        self.lst = lst  # Example shared variable
        self.lst_selected = lst_selected  # Example shared variable

        self.frame_navig = FrameNavig(self)
        self.frame_navig.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.mainframe = ctk.CTkFrame(self)

        self.labelMain = ctk.CTkLabel(self.mainframe, text="Interface de configuration", font=("Courrier", 25, "bold"))
        self.labelMain.grid(row=0, padx=20, pady=10)

        self.mainframe.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

        self.frames = {}
        self.create_frames()

        # self.frames[FrameGuideCapteurs] = FrameGuideCapteurs(self.mainframe)
        #
        #
        # for F in (FrameConfig,FrameConfigAdvance, FrameBoutons, FrameMonProfil, FrameNervegear):
        #     self.frames[F] = F(self.mainframe)
        #     self.frames[F].grid(row=0, column=0, sticky="nsew")
        # self.show_frame(FrameConfig)

        self.text_widget = Text(self.frames["FrameConfig"], height=1, width=5)
        self.text_widget.grid(row=1, column=0, padx=0, pady=30, sticky="ne")
        self.text_widget.bind("<Return>", self.paste_config_code)

        self.button_copy_code = ctk.CTkButton(self.frames["FrameConfig"], text="Copy Config Code",
                                              command=self.copy_config_to_clipboard)
        self.button_copy_code.grid(row=1, column=1, padx=(20, 20), pady=20, sticky="ne")

        # Place the dropdown menu for window selection
        self.dropdown = ctk.CTkOptionMenu(self.frames["FrameConfig"], values=self.window_list,
                                          variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, column=2, padx=(0, 20), pady=20, sticky="ne")

        self.dropdown = ctk.CTkOptionMenu(self.frames["FrameConfigAdvance"], values=self.window_list,
                                          variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, padx=20, pady=20, sticky = "ne")

        self.dropdown = ctk.CTkOptionMenu(self.frames["FrameBoutons"], values=self.window_list,
                                          variable=self.selected_window, command=self.update_minecraft_window)
        self.dropdown.grid(row=1, padx=20, pady=20, sticky="ne")

    def create_frames(self):
        self.frames["FrameGuideCapteurs"] = FrameGuideCapteurs(self.mainframe)
        self.frames["FrameConfig"] = FrameConfig(self.mainframe, self)
        self.frames["FrameConfigAdvance"] = FrameConfigAdvance(self.mainframe, self)
        self.frames["FrameBoutons"] = FrameBoutons(self.mainframe, self)
        self.frames["FrameMonProfil"] = FrameMonProfil(self.mainframe)
        self.frames["FrameNervegear"] = FrameNervegear(self.mainframe)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FrameConfig")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        
    def update_minecraft_window(self, *args):
        selected_window = self.selected_window.get()
        MC.set_window_name(selected_window)
        print(f"Updated Minecraft window to: {selected_window}")

    def get_selected_window(self):
        return self.selected_window.get()

    def copy_config_to_clipboard(self):
        config_path = "../ConfigEngine/selected_options.txt"
        config_code = ConfigEncryption.config_to_code(config_path)
        pyperclip.copy(config_code)
        self.frames["FrameConfig"].show_error("Configuration copiée avec succès")

    def paste_config_code(self, event):
        print("J APPUIIIIIIIIIIIIIIIIIIIS")
        configuration_path = "../ConfigEngine/selected_options.txt"
        code = self.text_widget.get("1.0", "end").strip()
        ConfigEncryption.code_to_config(code, configuration_path)
        self.frames["FrameConfig"].show_error("Configuration collée avec succès")
        app.lst_selected = load_selected_options()
        print ("liste ds paste : ",app.lst_selected)
        app.frames["FrameConfig"].update_optionmenu()
        app.frames["FrameConfig"].update()

        #print("ds frame", str(app.frames["FrameConfig"].self.app.lst_selected))

        #app.frames["FrameConfig"].list.e.update()



class FrameNavig(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.app = master

        self.frame_start = ctk.CTkFrame(self)
        # brouillon : ici faire fonction de choix des autres fcts
        # self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: MuscleTracking(MC.mouvement_clic_muscle, MC.mouvement_saut_muscle),
        # self.frame_start.button = ctk.CTkSwitch(master=self.frame_start, text="Tracking", command=lambda: StartAllTracking(),
        # onvalue="on", offvalue="off")

        self.switch_var = ctk.BooleanVar(value=False)
        self.buttonTracking = ctk.CTkSwitch(master=self.frame_start, text="Tracking",
                                            variable=self.switch_var,
                                            # command = lambda: switch(),
                                            command=lambda: check_and_start_tracking(self),
                                            onvalue=True, offvalue=False)

        self.frame_start.pack(pady=20, padx=20)
        self.buttonTracking.pack(pady=20, padx=30)
        self.button1 = ctk.CTkButton(self, text="Configuration", command=lambda: master.show_frame("FrameConfig"))
        self.button1.pack(pady=20, padx=20)

        self.button12 = ctk.CTkButton(self, text="Configuration Avancée",
                                      command=lambda: master.show_frame("FrameConfigAdvance"))
        self.button12.pack(pady=20, padx=20)

        self.button2 = ctk.CTkButton(self, text="Test Commandes", command=lambda: master.show_frame("FrameBoutons"))
        self.button2.pack(pady=20, padx=20)

        self.button_guide = ctk.CTkButton(self, text="Guide capteurs",
                                          command=lambda: master.show_frame("FrameGuideCapteurs"))
        self.button_guide.pack(pady=20, padx=20)

        self.button_profil = ctk.CTkButton(self, text="Mon profil", command=lambda: master.show_frame("FrameMonProfil"))
        self.button_profil.pack(pady=20, padx=20)

        self.button_nervegear = ctk.CTkButton(self, text="Nervegear",
                                              command=lambda: master.show_frame("FrameNervegear"))
        self.button_nervegear.pack(pady=20, padx=20)

def check_and_start_tracking(self):
    if app.frames["FrameConfig"].buttonActivate.get() == False and app.frames["FrameConfigAdvance"].buttonActivate.get() == False:
        print("2 FALSE")
        app.frames["FrameConfig"].show_error("Vous devez activer au moins une configuration (bouton Activer)")
        app.frames["FrameConfigAdvance"].show_error("Vous devez activer au moins une configuration (bouton Activer)")
        self.buttonTracking.deselect()



    elif app.frames["FrameConfig"].buttonActivate.get() == True:
        print("choix config 1\n\n")
        if app.selected_window.get() == "Choisir fenêtre":
            app.frames["FrameConfig"].show_error("Vous n'avez saisi aucune fenêtre de jeu")
            self.buttonTracking.deselect()
        elif isChoicesValid():
             StartAllTracking()
             app.frames["FrameConfig"].show_error("")
        else:
            app.frames["FrameConfig"].show_error("Certains choix sont invalides")
            bouton_trouve = self.buttonTracking

            if bouton_trouve is not None:
                bouton_trouve.deselect()
                print(bouton_trouve)




    elif app.frames["FrameConfigAdvance"].buttonActivate.get() == True:
        print("choix config 2\n\n")
        toucheAndCapteurs = app.frames["FrameConfigAdvance"].get_touches_and_capteurs()
        if app.selected_window.get() == "Choisir fenêtre":
            app.frames["FrameConfigAdvance"].show_error("Vous n'avez saisi aucune fenêtre de jeu")
            self.buttonTracking.deselect()

        elif  all_touches_empty(self, toucheAndCapteurs):
            app.frames["FrameConfigAdvance"].show_error("Vous n'avez saisi aucune touche")
            self.buttonTracking.deselect()
        elif all_capteurs_empty(self,toucheAndCapteurs):
            app.frames["FrameConfigAdvance"].show_error("Vous n'avez saisi aucun capteur")
            self.buttonTracking.deselect()
        elif has_touche_without_capteur(self,toucheAndCapteurs):
            self.buttonTracking.deselect()
        elif has_duplicate_capteur(self,toucheAndCapteurs):
            self.buttonTracking.deselect()
        else:
            clear_error(self)
            StartAllTracking()

def all_touches_empty(self, toucheAndCapteurs):
    return all(touche == '' for touche, _ in toucheAndCapteurs)

def all_capteurs_empty(self, toucheAndCapteurs):
    return all(capteur == 'Veuillez choisir' for _, capteur in toucheAndCapteurs)

def has_touche_without_capteur(self, toucheAndCapteurs):
    doublons = {}
    for touche, capteur in toucheAndCapteurs:
        if touche != '' and capteur == 'Veuillez choisir':
            if touche in doublons:
                doublons[touche] += 1
            else:
                doublons[touche] = 1
    if doublons:
        for touche, count in doublons.items():
            app.frames["FrameConfigAdvance"].show_error(
                "Le capteur associé à la touche '{}' ne peut pas être 'Veuillez choisir'.".format(touche))
        return True
    return False

def has_duplicate_capteur(self, toucheAndCapteurs):
    lst_capt_used = []
    doublons = {}
    for touche, capteur in toucheAndCapteurs:
        if touche != '':
            lst_capt_used.append(capteur)
    for capteur in lst_capt_used:
        if lst_capt_used.count(capteur) > 1:
            if capteur not in doublons:
                doublons[capteur] = 1
            else:
                doublons[capteur] += 1
    if doublons:
        for capteur, count in doublons.items():
            app.frames["FrameConfigAdvance"].show_error(
                "Le capteur '{}' est sélectionné plusieurs fois.".format(capteur))
        return True
    return False

def clear_error(self):
    app.frames["FrameConfig"].show_error("")
    app.frames["FrameConfigAdvance"].show_error("")

def show_error(self, message):
    app.frames["FrameConfigAdvance"].show_error(message)

def some_function(self):
    if app.frames["FrameConfigAdvance"].buttonActivate.get():
        self.check_touches_and_capteurs()
    else:
        self.clear_error()



def isChoicesValid():
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

    sensor_methode: Dict[str, List[Any]] = {
        "Accelerometre": [],
        "Camera": [],
        "EEG": [],
        "EMG": [],
        "ECG": []
    }

    val = []


    if app.frames["FrameConfigAdvance"].buttonActivate.get() == True :
        print("choix2")
        user_choices = app.frames["FrameConfigAdvance"].get_touches_and_capteurs()
        print("valllllll",user_choices)

        def analyze_user_choices(choices):
            camera_choices = {
                'tete': {'gauche': None, 'droite': None, 'milieu': None},
                'doigt': {str(i): None for i in range(1, 10)}
            }

            for key, action in choices:
                if 'Camera' in action:
                    if 'mouvement de tete' in action:
                        if 'gauche' in action:
                            camera_choices['tete']['gauche'] = key
                        elif 'droite' in action:
                            camera_choices['tete']['droite'] = key
                        elif 'milieu' in action:
                            camera_choices['tete']['milieu'] = key
                    elif 'doigts' in action:
                        for i in range(1, 10):
                            if str(i) in action:
                                camera_choices['doigt'][str(i)] = key
                                break
            return camera_choices

        def launch_camera_sensors(camera_config):
            def create_lambda(key):
                return lambda: MC.activate_key(key)
            # Lancer la détection de mouvement de tête si nécessaire
            if any(camera_config['tete'].values()):
                print("Lancer la détection de mouvement de tête avec les configurations suivantes:")
                func_action_gauche = None
                func_action_droit = None
                func_action_milieu = None

                for direction, key in camera_config['tete'].items():
                    if key:
                        print(f"Mouvement de tête {direction}: touche {key}")
                        if direction == "gauche":
                            func_action_gauche = create_lambda(key)
                        elif direction == "droite":
                            func_action_droit = create_lambda(key)
                        elif direction == "milieu":
                            func_action_milieu = create_lambda(key)
                # Lancer la détection de mouvement de tête ici
                #print("Function for func_action_droit:", inspect.getsource(func_action_droit)) marche pas

                HeadAndHandTracking(func_action_gauche, func_action_droit, func_action_milieu, None)
                #lancer HeadAndHandTracking(func_action_gauche=None, func_action_droit=None, func_action_milieu=None,
                        #func_action_doigts=None):

                #Savoir quoi mettre à la place de func_action_droite : si la direction et droite : récupérer la key associé et faire activate_key() avec celle la
                #etc avec les autres func

            # Lancer la détection de mouvement des doigts si nécessaire
            if any(camera_config['doigt'].values()):
                print("Lancer la détection de mouvement des doigts avec les configurations suivantes:")
                for finger, key in camera_config['doigt'].items():
                    if key:
                        print(f"Mouvement de doigt {finger}: touche {key}")
                # Lancer la détection de mouvement des doigts ici


            # Lancer la détection de mouvement de tête et des doigts si nécessaire

            #A FAIRE


        # Analyse des choix de l'utilisateur
        camera_config = analyze_user_choices(user_choices)
        print("\n\nCONFIG" , camera_config)

        # Lancer les capteurs avec les configurations appropriées
        launch_camera_sensors(camera_config)



    elif app.frames["FrameConfig"].buttonActivate.get() == True :
        print("choix1")
        val = load_selected_options()

        # Accelerometre
        # Veuillez
        # choisir
        # Veuillez
        # choisir
        # Veuillez
        # choisir
        # Camera - doigts




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
                if sensor == "Accelerometre":
                    tabthread.append(start_accelerometre(sensor_methode["Accelerometre"],*uses))
                    #tabthread.append(start_accelerometre(methodes=sensor_methode["Accelerometre"],*uses ))
                elif sensor == "Camera":
                    tabthread.append(start_camera(sensor_methode["Camera"], *uses))
                elif sensor == "EEG":
                    tabthread.append(start_eeg(sensor_methode["EEG"],*uses))
                elif sensor == "EMG":
                    tabthread.append(start_emg(sensor_methode["EMG"], *uses))
                elif sensor == "ECG":
                    tabthread.append(start_ecg(sensor_methode["ECG"],*uses))

        with Pool(cpu_count()) as pool:
            pool.map_async(lambda f: f(), tabthread)
            pool.close()
            pool.join()

        # for thread in tabthread:
        #     print("Démarrage du thread", thread.name)
        #     thread.start()
        #
        # for thread in tabthread:
        #     thread.join()
        print("Fin de la configuration des capteurs")

    print("FIN START ALL TRACKING")

def start_camera(methodes=None, *usages ):
    #Déplacement / changer d'objet avec main ou eye tracking

    if len(usages) == 1 and methodes[0].strip()=="Camera":
        HeadAndHandTracking(
            lambda: MC.mouvement_gauche_droite_cam("gauche"),
            lambda: MC.mouvement_gauche_droite_cam("droite"),
            lambda: MC.mouvement_gauche_droite_cam("milieu"),
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


def start_accelerometre(methodes=None, *usages):
    print("start_accelerometre")
    if len(usages) == 1 and methodes[0].strip()=="Accelerometre":
        AccelerometreTracking(
            lambda: MC.mouvement_av(),
            lambda: MC.mouvement_gav(),
            lambda: MC.mouvement_dav(),
            lambda: MC.mouvement_ar(),
            lambda: MC.mouvement_gar(),
            lambda: MC.mouvement_dar(),
            lambda: MC.mouvement_g(),
            lambda: MC.mouvement_d(),
            lambda: MC.mouvement_stop(),
            lambda: MC.mouvement_saut()
        )

    #Deplacement
    print("Démarrage de l'accéléromètre.")
    for usage in usages:
        print(f"Utilisation de l'accéléromètre pour : {usage}")

    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")


def start_eeg( methodes=None,*usages):
    #Sauter
    print("Démarrage de l'EEG.")
    for usage in usages:
        print(f"Utilisation de l'EEG pour : {usage}")
    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")

def start_emg(methodes=None, *usages,):
    #sauter avec 1 ou 2 implusions , cliquer avec 1 ou 2 implusions
    print("EMG")
    if len(usages)==1 and usages[0] =="Sauter" :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(lambda: MC.mouvement_saut_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(None, lambda: MC.mouvement_saut_muscle)

    elif len(usages)==1 and usages[0] =="Clique souris" :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(lambda: MC.mouvement_clic_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(None, lambda: MC.mouvement_clic_muscle)

    elif len(usages)==2 :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(lambda: MC.mouvement_saut_muscle, lambda: MC.mouvement_clic_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(lambda: MC.mouvement_clic_muscle, lambda: MC.mouvement_saut_muscle)



def start_ecg(methodes=None, *usages):
    #vitesse
    print("Démarrage de l'ECG.")
    for usage in usages:
        print(f"Utilisation de l'ECG pour : {usage}")
    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")

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


#definition du mapping
if __name__ == "__main__":
    # appeler fichiers ds capteurs selon la configuration

    lst =load_config('../ConfigEngine/config.csv')
    lst_selected = load_selected_options()
    total_rows = len(lst)


    app = App()
    app.lst = lst
    app.lst_selected = lst_selected
    print("home liste selected : "+str(app.lst_selected))
    app.total_rows = total_rows

    app.mainloop()