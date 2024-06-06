import customtkinter as ctk

from Interface.CapteursEngine.AccelerometreEngine import AccelerometreTracking
from Interface.CapteursEngine.BitalinoEngine import MuscleTracking
from Interface.CapteursEngine.TestCameraRecognition import HeadAndHandTracking
from typing import Dict, List, Any
from multiprocessing import Pool, cpu_count

from Interface.WindowInterface.utils import load_selected_options


class FrameNavig(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.app = master

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
        self.button1 = ctk.CTkButton(self, text="Configuration", command=lambda: master.show_frame("FrameConfig"))
        self.button1.pack(pady=20, padx=20)

        self.button12 = ctk.CTkButton(self, text="Configuration Avancée", command=lambda: master.show_frame("FrameConfigAdvance"))
        self.button12.pack(pady=20, padx=20)

        self.button2 = ctk.CTkButton(self, text="Test Commandes", command=lambda: master.show_frame("FrameBoutons"))
        self.button2.pack(pady=20, padx=20)

        self.button_guide = ctk.CTkButton(self, text="Guide capteurs", command=lambda: master.show_frame("FrameGuideCapteurs"))
        self.button_guide.pack(pady=20, padx=20)

        self.button_profil = ctk.CTkButton(self, text="Mon profil", command=lambda: master.show_frame("FrameMonProfil"))
        self.button_profil.pack(pady=20, padx=20)

        self.button_nervegear = ctk.CTkButton(self, text="Nervegear", command=lambda: master.show_frame("FrameNervegear"))
        self.button_nervegear.pack(pady=20, padx=20)


def check_and_start_tracking(self):


    if self.app.frames["FrameConfig"].buttonActivate.get() == False and self.app.frames["FrameConfigAdvance"].buttonActivate.get() == False:
        print("2 FALSE")
        self.app.frames["FrameConfig"].show_error("Vous devez activer au moins une configuration (bouton Activer)")
        self.app.frames["FrameConfigAdvance"].show_error("Vous devez activer au moins une configuration (bouton Activer)")
        self.buttonTracking.deselect()



    elif self.app.frames["FrameConfig"].buttonActivate.get() == True:
        print("choix config 1\n\n")
        if isChoicesValid():
             StartAllTracking()
             self.app.frames["FrameConfig"].show_error("")
        else:
            self.app.frames["FrameConfig"].show_error("Certains choix sont invalides")
            bouton_trouve = self.buttonTracking

            if bouton_trouve is not None:
                bouton_trouve.deselect()
                print(bouton_trouve)




    elif self.app.frames["FrameConfigAdvance"].buttonActivate.get() == True:
        print("choix config 2\n\n")
        toucheAndCapteurs = self.app.frames["FrameConfigAdvance"].get_touches_and_capteurs()

        if  all_touches_empty(self, toucheAndCapteurs):
            self.app.frames["FrameConfigAdvance"].show_error("Vous n'avez saisi aucune touche")
            self.buttonTracking.deselect()
        elif all_capteurs_empty(self,toucheAndCapteurs):
            self.app.frames["FrameConfigAdvance"].show_error("Vous n'avez saisi aucun capteur")
            self.buttonTracking.deselect()
        elif has_touche_without_capteur(self,toucheAndCapteurs):
            self.buttonTracking.deselect()
        elif has_duplicate_capteur(self,toucheAndCapteurs):
            self.buttonTracking.deselect()
        else:
            clear_error(self)

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
            self.app.frames["FrameConfigAdvance"].show_error(
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
            self.app.frames["FrameConfigAdvance"].show_error(
                "Le capteur '{}' est sélectionné plusieurs fois.".format(capteur))
        return True
    return False

def clear_error(self):
    self.app.frames["FrameConfig"].show_error("")
    self.app.frames["FrameConfigAdvance"].show_error("")

def show_error(self, message):
    self.app.frames["FrameConfigAdvance"].show_error(message)

def some_function(self):
    if self.app.frames["FrameConfigAdvance"].buttonActivate.get():
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

    sensor_methode: Dict[str, List[Any]] = {
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

def start_camera(self, methodes=None, *usages ):
    #Déplacement / changer d'objet avec main ou eye tracking

    if len(usages) == 1 and methodes[0].strip()=="Camera":
        HeadAndHandTracking(
            lambda: self.app.MC.mouvement_gauche_droite_cam("gauche"),
            lambda: self.app.MC.mouvement_gauche_droite_cam("milieu"),
            lambda: self.app.MC.mouvement_gauche_droite_cam("droite"),
            None
        )

    elif len(usages) ==1 and methodes[0].strip()=="Camera - doigts":
        HeadAndHandTracking(
            None,
            None,
            None,
            lambda number: self.app.MC.changer_barre(number)
        )

    elif len(usages) ==1 and methodes[0].strip=="Camera - Eye tracking":
        #todo eye tracking
        print("TO DO EYE TRACKING")

    elif len(usages) == 2:
        if methodes[1].strip() == "Camera - doigts":
            HeadAndHandTracking(
                lambda: self.app.MC.mouvement_gauche_droite_cam("gauche"),
                lambda: self.app.MC.mouvement_gauche_droite_cam("milieu"),
                lambda: self.app.MC.mouvement_gauche_droite_cam("droite"),
                lambda number: self.app.MC.changer_barre(number)
            )
        else:
            # todo eye tracking
            print("TO DO EYE TRACKING")


def start_accelerometre(self, methodes=None, *usages):
    print("start_accelerometre")
    if len(usages) == 1 and methodes[0].strip()=="Accelerometre":
        AccelerometreTracking(
            lambda: self.app.MC.mouvement_av(),
            lambda: self.app.MC.mouvement_gav(),
            lambda: self.app.MC.mouvement_dav(),
            lambda: self.app.MC.mouvement_ar(),
            lambda: self.app.MC.mouvement_gar(),
            lambda: self.app.MC.mouvement_dar(),
            lambda: self.app.MC.mouvement_g(),
            lambda: self.app.MC.mouvement_d(),
            lambda: self.app.MC.mouvement_stop(),
            lambda: self.app.MC.mouvement_saut()
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

def start_emg(self, methodes=None, *usages,):
    #sauter avec 1 ou 2 implusions , cliquer avec 1 ou 2 implusions
    print("EMG")
    if len(usages)==1 and usages[0] =="Sauter" :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(lambda: self.app.MC.mouvement_saut_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(None, lambda: self.app.MC.mouvement_saut_muscle)

    elif len(usages)==1 and usages[0] =="Clique souris" :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(lambda: self.app.MC.mouvement_clic_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(None, lambda: self.app.MC.mouvement_clic_muscle)

    elif len(usages)==2 :
        if methodes[0] == "EMG - bras 1 impulsion" :
            MuscleTracking(lambda: self.app.MC.mouvement_saut_muscle, lambda: self.app.MC.mouvement_clic_muscle)
        if methodes[0] == "EMG - bras 2 impulsions"  :
            MuscleTracking(lambda: self.app.MC.mouvement_clic_muscle, lambda: self.app.MC.mouvement_saut_muscle)



def start_ecg(methodes=None, *usages):
    #vitesse
    print("Démarrage de l'ECG.")
    for usage in usages:
        print(f"Utilisation de l'ECG pour : {usage}")
    if methodes:
        print("Méthodes spécifiques :")
        for methode in methodes:
            print(f"- {methode}")

